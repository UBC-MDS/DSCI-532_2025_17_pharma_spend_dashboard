# Test src/callbacks/ scripts 
# Date: March 13, 2025
# Authors: Daria Khon, Catherine Meng, Jason Lee, Celine Habashy

from dash import Dash, dcc, html
from flask_caching import Cache
import geopandas as gpd
import pytest
from shapely.geometry import MultiPolygon, Polygon
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.callbacks.charts import charts_callback

@pytest.fixture
def test_data():
    """Pytest fixture for test geodata"""
    return gpd.GeoDataFrame({
        'name': ['United States of America', 'Canada'],
        'geometry': [
            MultiPolygon([Polygon([(147.68926, -40.80826), (148, -41), (147, -41), (147.68926, -40.80826)])]),
            MultiPolygon([Polygon([(-122.84003, 49.00114), (-123, 49), (-122, 49), (-122.84003, 49.00114)])])
        ],
        'LOCATION': ['USA', 'CAN'],
        'TIME': [2020, 2020],
        'PC_HEALTHXP': [5, 7],
        'PC_GDP': [10, 80],
        'USD_CAP': [100, 300],
        'TOTAL_SPEND': [500, 60]
    }, geometry='geometry')

@pytest.fixture
def dash_app():
    """Pytest fixture for dashboard"""
    app = Dash(__name__)

    app.layout = [
        dcc.Dropdown(id='country_select', options=[{'label': 'Canada', 'value': 'United States of America'}]),
        dcc.Dropdown(id='start_year_select', options=[{'label': '2000', 'value': 2000}, {'label': '2005', 'value': 2005}]),
        dcc.Dropdown(id='end_year_select', options=[{'label': '2010', 'value': 2010}, {'label': '2015', 'value': 2015}]),
        dcc.RadioItems(id='spend_metric',options=[
            {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
            {'label': 'TOTAL SPEND', 'value': 'TOTAL_SPEND'}
        ],value='PC_HEALTHXP'),
        dcc.Graph(id='map_chart'),
        dcc.Graph(id='timeseries_chart'),
        dcc.Graph(id='bar_chart')
    ]
    
    cache = Cache(app.server, config={'CACHE_TYPE': 'simple'}) 
    return app, cache

def test_callbacks(dash_app, test_data):
    """Test dashboard callbacks: (1) if they return chart objects and if caching works """
    app, cache = dash_app
    
    # user inputs
    n_clicks = 1
    country_select = ["United States of America", "Canada"]
    start_year = 2000
    end_year = 2020
    spend_metric = "PC_HEALTHXP"
    spend_metric_options = [
                        {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
                        {'label': 'Total Spend (USD B)', 'value': 'TOTAL_SPEND'},
                    ]
    
    create_chart = charts_callback(test_data, cache) 
    
    map_chart, time_series_chart, bar_chart, map_title, ts_title, bar_title = create_chart(
        n_clicks, country_select, start_year, end_year, spend_metric, spend_metric_options
    )
    
    assert map_chart is not None, "Map chart should not be None"
    assert isinstance(time_series_chart, dict), "Time series chart should not be a dictionary"
    assert isinstance(bar_chart, dict), "Bar chart should be a dictionary"
    
    cached_func = cache.memoize()(lambda x: x) 
    result1 = cached_func(42)
    result2 = cached_func(42) 

    assert result1 == result2, "Cache is not storing values properly"
