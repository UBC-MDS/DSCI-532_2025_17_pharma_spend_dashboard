# Test src/components/sidebar.py script 
# Date: March 13, 2025
# Authors: Daria Khon, Catherine Meng, Jason Lee, Celine Habashy
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.components.sidebar import create_sidebar
from dash import html, dcc
import dash_bootstrap_components as dbc

@pytest.fixture
def test_data():
    """Pytest fixture to create test geodata"""
    return {
        "locations": ["Canada", "United States of America", "Mexico"],
        "times": list(range(2000, 2025)),
        "min_year": 2000,
        "max_year": 2024
    }

def test_create_sidebar_structure(test_data):
    """Test side bar implementation """
    sidebar = create_sidebar(**test_data)
    
    assert isinstance(sidebar, dbc.Col), "Sidebar should be a dbc.Col component"
    assert any(isinstance(comp, dcc.Dropdown) and comp.id == 'country_select' for comp in sidebar.children), "Country dropdown is missing"
    assert any(isinstance(comp, dcc.Dropdown) and comp.id == 'start_year_select' for comp in sidebar.children), "Start year dropdown is missing"
    assert any(isinstance(comp, dcc.Dropdown) and comp.id == 'end_year_select' for comp in sidebar.children), "End year dropdown is missing"
    assert any(isinstance(comp, dcc.RadioItems) and comp.id == 'spend_metric' for comp in sidebar.children), "Spend metric radio items are missing"
    assert any(isinstance(comp, dbc.Button) and comp.id == 'submit_button' for comp in sidebar.children), "Submit button is missing"


