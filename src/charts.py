from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import geopandas as gpd
import altair as alt
import sys
import os
from datetime import datetime

def create_map_chart(filtered_data_merged, spend_metric, spend_metric_label):
    """
    Creates a map chart
    """
    map = alt.Chart(filtered_data_merged, width=400).mark_geoshape(stroke='white', color='lightgrey').encode()    
    chart = alt.Chart(filtered_data_merged).mark_geoshape().encode(
        color = alt.Color(
            spend_metric,
            scale = alt.Scale(scheme='teals'),
            legend=alt.Legend(title=f'Average {spend_metric_label}')
        ),
        tooltip = 'LOCATION'
    ).project(
        'naturalEarth1'
    )
    
    bubbles = alt.Chart(filtered_data_merged).transform_calculate(
        centroid=alt.expr.geoCentroid(None, alt.datum)
    ).mark_circle(
        stroke='brown',
        fill = 'brown',
        strokeWidth = 1,
        opacity = 0.5
    ).encode(
        longitude='centroid[0]:Q',
        latitude='centroid[1]:Q',
        size=alt.Size(spend_metric, 
                  legend=alt.Legend(title=None)),
        tooltip = alt.Tooltip(spend_metric, format=".2f")
    )
    map_chart = map + chart + bubbles

    return map_chart

def create_time_chart(filtered_data, spend_metric, spend_metric_label, start_year_select, end_year_select):
    """
    Creates a time series chart
    """
    line = alt.Chart(filtered_data).mark_line().encode(
        x=alt.X('TIME:Q', title="Year").axis(format="d"),
        y=alt.Y(spend_metric, title=f"{spend_metric_label}"),
        color=alt.Color('LOCATION', legend=alt.Legend(title="Country")),
        tooltip=['LOCATION', spend_metric]
    )

    points = alt.Chart(filtered_data).mark_circle().encode(
        x=alt.X('TIME:Q'),
        y=alt.Y(spend_metric),
        color='LOCATION',  # Keeps color consistent with the line chart
        tooltip=['LOCATION', spend_metric]
    )

    timeseries_chart = (line + points).properties(
        title= f'{spend_metric_label} by Country ({start_year_select} to {end_year_select})'
    )

    return timeseries_chart

def create_bar_chart(avg_data, spend_metric, spend_metric_label):
    """
    Creates a bar chart
    """    
    bar_chart = alt.Chart(avg_data).mark_bar(color="steelblue").encode(
        x=alt.X(f'mean({spend_metric}):Q', title="Total Spend (USD)"),
        y=alt.Y('LOCATION:N', title="Country", sort='-x'),  
        tooltip=['LOCATION', f'mean({spend_metric})']
    ).properties(
        title=f"Average {spend_metric_label} by Country",
        height = 250
    )
    return bar_chart

def create_pie_chart(avg_data, spend_metric, spend_metric_label):
    """
    Creates a pie chart
    """
    pie_chart = alt.Chart(avg_data).mark_arc().encode(
        theta=alt.Theta(field=spend_metric, type='quantitative', stack=True),
        color=alt.Color(field='LOCATION', type='nominal', legend=alt.Legend(title="Country")),
        tooltip=['LOCATION', spend_metric]
    ).properties(
        title=f'Average {spend_metric_label} by Country'
    )
    return pie_chart