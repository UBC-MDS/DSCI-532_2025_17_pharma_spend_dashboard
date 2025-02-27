from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Data preprocessing
data = pd.read_csv('data/raw/data.csv')
data = data.drop('FLAG_CODES', axis=1)

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
            value=data['TIME'].min(),  # Default start by the minimal year
            clearable=False
        ),
        html.P('To', style={'marginTop': '0.375rem'}),
        dcc.Dropdown(
            id='end_year_select',
            options=[{'label': str(year), 'value': year} for year in times],
            value=data['TIME'].max(),  # Default end by the maximum year
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

card_style = {'height': '100px'}

# Summary status (Celine)
summary = dbc.Row(
    [
        html.H5('Summary Stats'),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5('Avg % GDP'),
                ])
            ], style=card_style), width=3),  # Takes 4/12 columns

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5('Avg % of Health Spending'),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5('Avg Spend per Capita (in USD)'),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5('Total Spend (in USD m)'),
                ])
            ], style=card_style), width=3),
        ])
    ],
    style = {'paddingBottom': '1rem'}
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
    Output('map_chart', 'spec'),
    Output('timeseries_chart', 'spec'),
    Output('bar_chart', 'spec'),
    Output('pie_chart', 'spec'),
    Input('country_select', 'value'),
    Input('start_year_select', 'value'),
    Input('end_year_select', 'value'),
    Input('spend_metric', 'value')
)
def create_chart(country_select, start_year_select, end_year_select, spend_metric):
    filtered_data = data[
        data['LOCATION'].isin(country_select) &  # Filter by selected countries
        data['TIME'].between(start_year_select, end_year_select)  # Filter TIME between years
    ]
    # Get average data group by country and year
    avg_data = filtered_data.groupby('LOCATION')[spend_metric].mean().reset_index()

    # Map Plot (Daria)
    map_chart = alt.Chart(filtered_data).mark_point().encode(
        x='TIME',
        y=spend_metric,
        color='LOCATION'
    )

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

    # Pie Chart (Catherine)
    pie_chart = alt.Chart(avg_data).mark_arc().encode(
        theta=alt.Theta(field=spend_metric, type='quantitative', stack=True),
        color=alt.Color(field='LOCATION', type='nominal'),
        tooltip=['LOCATION', spend_metric]
    ).properties(
        title=f'Average {spend_metric} by Country'
    )

    return map_chart.to_dict(), timeseries_chart.to_dict(), bar_chart.to_dict(), pie_chart.to_dict()

if __name__ == '__main__':
    app.run()

