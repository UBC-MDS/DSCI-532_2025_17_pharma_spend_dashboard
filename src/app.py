from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import geopandas as gpd
import altair as alt
import sys
import os
# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
from src.preprocessing import preprocess

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Data preprocessing
data, world_countries = preprocess("data/raw/data.csv")
print("Data Loading Success!")
# get the locations and years from the original dataset
locations = data['LOCATION'].unique()
times = sorted(data['TIME'].unique()) # integer type
min_year = data['TIME'].min()
max_year = data['TIME'].max()

# Side bar for global filter
sidebar = dbc.Col(
    [
        html.H3('Global Pharmaceutical Spend Dashboard'),
        html.Br(),

        html.H5('Country'),
        dcc.Dropdown(
            id='country_select', 
            options=[{'label': country, 'value': country} for country in locations], 
            value=['CAN', 'USA', 'MEX'], 
            multi=True
        ),
        html.Br(),

        html.H5('Year'),
        html.P('From', style={'marginBottom': '0.375rem'}),
        dcc.Dropdown(
            id='start_year_select',
            options=[{'label': str(year), 'value': year} for year in times],
            value=min_year,  # Default start by the minimal year
            clearable=False
        ),
        html.P('To', style={'marginTop': '0.375rem'}),
        dcc.Dropdown(
            id='end_year_select',
            options=[{'label': str(year), 'value': year} for year in times],
            value=max_year,  # Default end by the maximum year
            clearable=False
        )
    ],
    md=3,
    style={
        'backgroundColor': '#e6e6e6',
        'padding': 15,  # Padding top,left,right,botoom
        'paddingLeft': 30,
        'width': '20vw',
        'minHeight': '100vh',  # vh = 'viewport height' = 100% of the window height
        'flexDirection': 'column',  # Allow for children to be aligned to bottom
    }
) 

card_style = {'height': '125px'}

# Summary status (Celine)
summary = dcc.Loading(
    children=dbc.Row(
        [
            html.H5('Summary Stats'),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg % GDP"),
                        html.H2(id="gdp-value", style={"fontWeight": "bold"}),  
                        html.P(id="gdp-growth", style={"color": "green", "fontSize": "14px"})  
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg % of Health Spending"),
                        html.H2(id="health-value", style={"fontWeight": "bold"}),
                        html.P(id="health-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg Spend per Capita (USD)"),
                        html.H2(id="capita-value", style={"fontWeight": "bold"}),
                        html.P(id="capita-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Total Spend (USD m)"),
                        html.H2(id="total-value", style={"fontWeight": "bold"}),
                        html.P(id="total-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),
            ])
        ],
        style={'paddingBottom': '1rem'}
    ),
    type="cube", fullscreen=False, color="white"
)

# Metric Selector
metric_selection = dbc.Row(
    [
        dbc.Col(html.H5('Spend Metrics'), width=2),
        dbc.Col(
            dcc.RadioItems(
                id='spend_metric',
                options=[
                    {'label': 'Avg % GDP', 'value': 'PC_GDP'},
                    {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
                    {'label': 'USD Per Capita', 'value': 'USD_CAP'},
                    {'label': 'Total Spend', 'value': 'TOTAL_SPEND'},
                ],
                value='TOTAL_SPEND',  # Default selection
                labelStyle={'display': 'inline-block', 'marginRight': '0.938rem'}
            ),
        )
    ],
    style = {'paddingBottom': '1rem'}
)

# Charts
map_chart = dvc.Vega(id='map_chart', spec={})
timeseries_chart = dvc.Vega(id='timeseries_chart', spec={})
bar_chart = dvc.Vega(id='bar_chart', spec={})
pie_chart = dvc.Vega(id='pie_chart', spec={})

# App layout
app.layout = dbc.Container(
    [
        dbc.Row([
            sidebar,
            dbc.Col([
                summary,
                metric_selection,
                dbc.Row([
                    dbc.Col(map_chart, width=6),
                    dbc.Col(timeseries_chart, width=6)
                ]),
                dbc.Row([
                    dbc.Col(bar_chart, width=6),
                    dbc.Col(pie_chart, width=6)
                ])
            ], style = {'paddingLeft': '1.25rem', 'paddingTop': '0.625rem'})
        ])
    ],
    fluid=True,
    style={'padding': 0}
)

@app.callback(
    Output('end_year_select', 'options'),
    Output('end_year_select', 'value'),
    Input('start_year_select', 'value'),
    Input('end_year_select', 'value'),
)
def update_end_year_select_options(start, end):
    # Ensure that the end year value cannot older than the start year
    # Filter years that are greater than or equal to start_year
    filtered_years = [year for year in times if year >= start]
    options = [{'label': str(year), 'value': year} for year in filtered_years]

    # Ensure the selected end year remains valid
    default_end_year = end if end in filtered_years else filtered_years[0]

    return options, default_end_year

@callback(
    Output("gdp-value", "children"),
    Output("health-value", "children"),
    Output("capita-value", "children"),
    Output("total-value", "children"),
    Output("gdp-growth", "children"),
    Output("health-growth", "children"),
    Output("capita-growth", "children"),
    Output("total-growth", "children"),

    Input("country_select", "value"),
    Input("start_year_select", "value"),
    Input("end_year_select", "value"),
    Input("spend_metric", "value"),
)
def update_summary(countries, year_from, year_to, spend_metric):
    filtered_data = data.query("LOCATION in @countries and @year_from <= TIME <= @year_to")

    if filtered_data.empty:
        return ["N/A"] * 8 + [{}] * 4  

    def calc_growth(metric):
        df = filtered_data.groupby("TIME")[metric].mean()
        return f"+{((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100:.1f}% Growth" if len(df) > 1 and df.iloc[0] != 0 else "0% Growth"

    # Compute summary stats
    gdp_value = f"{filtered_data['PC_GDP'].mean():.2f}%"
    health_value = f"{filtered_data['PC_HEALTHXP'].mean():.2f}%"
    capita_value = f"${filtered_data['USD_CAP'].mean():,.2f}"
    total_value = f"${filtered_data['TOTAL_SPEND'].mean():,.2f}M"

    # growth_values = [
    #     calc_growth("PC_GDP"),
    #     calc_growth("PC_HEALTHXP"),
    #     calc_growth("USD_CAP"),
    #     calc_growth("TOTAL_SPEND")
    # ]
    
    return gdp_value, health_value, capita_value, total_value, calc_growth("PC_GDP"), calc_growth("PC_HEALTHXP"), calc_growth("USD_CAP"), calc_growth("TOTAL_SPEND")

@callback(
    Output('map_chart', 'spec'),
    Output('timeseries_chart', 'spec'),
    Output('bar_chart', 'spec'),
    Output('pie_chart', 'spec'),
    Input('country_select', 'value'),
    Input('start_year_select', 'value'),
    Input('end_year_select', 'value'),
    Input('spend_metric', 'value'),
    Input('spend_metric', 'options')
)
def create_chart(country_select, start_year_select, end_year_select, spend_metric, spend_metric_options):
    # Filter data by countries and years
    filtered_data = data[
        data['LOCATION'].isin(country_select) &  # Filter by selected countries
        data['TIME'].between(start_year_select, end_year_select)  # Filter TIME between years
    ]
    # Get average data group by country and year
    avg_data = filtered_data.groupby('LOCATION')[spend_metric].mean().reset_index()
    spend_metric_label = next(item['label'] for item in spend_metric_options if item['value'] == spend_metric)

    # Map Plot (Daria)
    # Merge average data with geometry
    filtered_data_merged = pd.merge(
        world_countries[['LOCATION', 'geometry', 'name']], 
        avg_data, 
        on='LOCATION', 
        how='left'
    )
    # More efficient for large data sets
    alt.data_transformers.enable('vegafusion')
    print("Finish preparing map data!")
    map = alt.Chart(filtered_data_merged, width=400).mark_geoshape(stroke='white', color='lightgrey').encode()    
    chart = alt.Chart(filtered_data_merged).mark_geoshape().encode(
        color = alt.Color(
            spend_metric,
            scale = alt.Scale(scheme='blues'),
            legend=alt.Legend(title=f'Average {spend_metric_label}')
        ))
    map_chart = map + chart

    # Time Series Chart (Jason)
    timeseries_chart = alt.Chart(filtered_data).mark_line().encode(
        x='TIME',
        y=spend_metric,
        color='LOCATION'
    )

    # Bar Chart (Celine)
    bar_chart = alt.Chart(filtered_data).mark_point().encode(
        x='TIME',
        y=spend_metric,
        color='LOCATION'
    )
    
    bar_chart = alt.Chart(avg_data).mark_bar(color="steelblue").encode(
        x=alt.X(f'mean({spend_metric}):Q', title="Total Spend (USD)"),
        y=alt.Y('LOCATION:N', title="Country", sort='-x'),  
        tooltip=['LOCATION', f'mean({spend_metric})']
    ).properties(
        title=f"Average {spend_metric_label} by Country",
        height = 250
    )
    
    # Pie Chart (Catherine)
    pie_chart = alt.Chart(avg_data).mark_arc().encode(
        theta=alt.Theta(field=spend_metric, type='quantitative', stack=True),
        color=alt.Color(field='LOCATION', type='nominal'),
        tooltip=['LOCATION', spend_metric]
    ).properties(
        title=f'Average {spend_metric_label} by Country'
    )

    return map_chart.to_dict(format="vega"), timeseries_chart.to_dict(format="vega"), bar_chart.to_dict(format="vega"), pie_chart.to_dict(format="vega")

if __name__ == '__main__':
    app.run(debug=True)

