from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import geopandas as gpd
import altair as alt
import sys
import os
from datetime import datetime

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
from src.preprocessing import preprocess
from src.charts import *

# Data preprocessing
data, world_countries = preprocess("data/raw/data.csv")
print("Data Loading Success!")
times = sorted(data['TIME'].unique()) # integer type

@callback(
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
    Output("gdp-growth", "style"),
    Output("health-growth", "children"),
    Output("health-growth", "style"),
    Output("capita-growth", "children"),
    Output("capita-growth", "style"),
    Output("total-growth", "children"),
    Output("total-growth", "style"),

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
        growth = ((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100
        
        if growth > 0:
            return f"+{growth:.1f}% Growth", {"color": "green"}
        else:
            return f"{growth:.1f}% Growth", {"color": "red"}

    # Compute summary stats
    gdp_value = f"{filtered_data['PC_GDP'].mean():.2f}%"
    health_value = f"{filtered_data['PC_HEALTHXP'].mean():.2f}%"
    capita_value = f"${filtered_data['USD_CAP'].mean():,.2f}"
    total_value = f"${int(filtered_data['TOTAL_SPEND'].mean()):,}"
    
    gdp_growth, gdp_growth_style = calc_growth("PC_GDP")
    health_growth, health_growth_style = calc_growth("PC_HEALTHXP")
    capita_growth, capita_growth_style = calc_growth("USD_CAP")
    total_growth, total_growth_style = calc_growth("TOTAL_SPEND")

    return (gdp_value, health_value, capita_value, total_value,
            gdp_growth, gdp_growth_style,
            health_growth, health_growth_style,
            capita_growth, capita_growth_style,
            total_growth, total_growth_style)



@callback(
    Output('map_chart', 'spec'),
    Output('timeseries_chart', 'spec'),
    Output('bar_chart', 'spec'),
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

    # Map Plot (Daria)
    map_chart = create_map_chart(filtered_data_merged, 
                                 spend_metric, 
                                 spend_metric_label)

    # Time Series Chart (Jason)
    timeseries_chart = create_time_chart(filtered_data, 
                                         spend_metric, 
                                         spend_metric_label, 
                                         start_year_select, 
                                         end_year_select)

    # Bar Chart (Celine)
    bar_chart = create_bar_chart(avg_data, 
                                 spend_metric, 
                                 spend_metric_label)

    return map_chart.to_dict(format="vega"), timeseries_chart.to_dict(format="vega"), bar_chart.to_dict(format="vega")