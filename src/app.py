from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import altair as alt

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv("../data/raw/data.csv")

# Side bar for global filter
sidebar = dbc.Col([
    html.H3('Global Pharmaceutical Spend Dashboard'),
    html.Br(),

    html.H5('Country'),
    dcc.Dropdown(id='country_select', options=[{'label': country, 'value': country} for country in data['LOCATION'].unique()], value=['CAN', 'USA', 'MEX'], multi=True),
    html.Br(),

    html.H5('Year'),
    html.P('From', style={'margin-bottom': '0.375rem'}),
    dcc.Dropdown(),
    html.P('To', style={'margin-top': '0.375rem'}),
    dcc.Dropdown(),
    ],
    md=3,
    style={
        'background-color': '#e6e6e6',
        'padding': 15,  # Padding top,left,right,botoom
        'padding-left': 30,
        'width': '20vw',
        'height': '100vh',  # vh = "viewport height" = 100% of the window height
        'flex-direction': 'column',  # Allow for children to be aligned to bottom
    }
) 

card_style = {'height': '100px'}

# Summary status
summary = dbc.Row(
    [
        html.H5('Summary Stats'),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg % GDP"),
                ])
            ], style=card_style), width=3),  # Takes 4/12 columns

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg % of Health Spending"),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg Spend per Capita (in USD)"),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Total Spend (in USD m)"),
                ])
            ], style=card_style), width=3),
        ])
    ],
    style={
        'padding': 15,
    }
)

#Metric Selector
metric_selection = dcc.RadioItems(
    id="radio-buttons",
    options=[
        {"label": "Avg % GDP", "value": "gdp"},
        {"label": "% of Healthcare", "value": "healthcare"},
        {"label": "Per Capita", "value": "per_capita"},
        {"label": "Total Spend", "value": "total_spend"},
    ],
    value="total_spend",  # Default selection
    labelStyle={'display': 'inline-block', 'margin-right': '15px'}
)

# Charts
line_chart1 = dvc.Vega(id="chart1", spec={})
line_chart2 = dvc.Vega(id="chart2", spec={})
line_chart3 = dvc.Vega(id="chart3", spec={})
line_chart4 = dvc.Vega(id="chart4", spec={})

# App layout
app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(sidebar, width=3),
            dbc.Col([
                summary,
                dbc.Row(metric_selection),
                dbc.Row([
                    dbc.Col(line_chart1, width=6),
                    dbc.Col(line_chart2, width=6)
                ]),
                dbc.Row([
                    dbc.Col(line_chart3, width=6),
                    dbc.Col(line_chart4, width=6)
                ])
            ], width=9)
        ])
    ],
    fluid=True,
    style={'padding': 0, 'margin': '10px'}
)

@callback(
    Output('chart1', 'spec'),
    Output('chart2', 'spec'),
    Output('chart3', 'spec'),
    Output('chart4', 'spec'),
    Input('country_select', 'value') 
    #Add one more input that controls Year (Daria)
)
def create_chart(country_select):
    filtered_data = data[data['LOCATION'].isin(country_select)]

    chart1 = alt.Chart(filtered_data).mark_point().encode(
            x='TIME',
            y='TOTAL_SPEND',
            color='LOCATION')

    chart2 = alt.Chart(filtered_data).mark_line().encode(
            x='TIME',
            y='TOTAL_SPEND',
            color='LOCATION')
    
    chart3 = alt.Chart(filtered_data).mark_point().encode(
            x='TIME',
            y='PC_GDP',
            color='LOCATION'
        )

    chart4 = alt.Chart(filtered_data).mark_point().encode(
            x='TIME',
            y='PC_HEALTHXP',
            color='LOCATION'
        )
    return chart1.to_dict(), chart2.to_dict(), chart3.to_dict(), chart4.to_dict()

if __name__ == '__main__':
    app.run(debug=True)

