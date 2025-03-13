from dash import Input, Output, callback
import plotly.express as px
import altair as alt

def tooltip_formatter(spend_metric_label):
    """
    Determines the appropriate tooltip format and value suffix 
    based on the selected spending metric.

    This function assigns a specific number formatting style to tooltips 
    depending on whether the spending metric is a percentage or a currency value.

    Parameters:
    -----------
    spend_metric_label : str
        The label of the selected spending metric.

    Returns:
    --------
    tuple (str, str)
        - tooltip_format (str): The formatting style for tooltip values 
          (e.g., ".2f" for percentages, "$,.2f" for currency).
        - value_suffix (str): The suffix to append to tooltip values 
          (e.g., "%" for percentages, "" for currency values).
    """
    
    if "GDP" in spend_metric_label or "Healthcare" in spend_metric_label:
        tooltip_format = ".2f"  # Percentage formatting
        value_suffix = "%"
    else:
        tooltip_format = "$,.2f"  # Currency formatting
        value_suffix = ""
    return tooltip_format, value_suffix

def title_formatter(spend_metric_label):
    """
    Formats chart titles based on the selected spending metric.

    This function maps specific spending metric labels to corresponding 
    descriptive chart titles.

    Parameters:
    -----------
    spend_metric_label : str
        The label of the selected spending metric.

    Returns:
    --------
    str
        A formatted title string for the corresponding chart.
    """

    if spend_metric_label == "% of GDP":
        return "Pharma Spend as a % of GDP"
    elif spend_metric_label == "% of Healthcare":
        return "Pharma Spend as a % of Healthcare"
    elif spend_metric_label == "Spend Per Capita (USD)":
        return "Pharma Spend Per Capita (USD)"
    elif spend_metric_label == "Total Spend (USD B)":
        return "Total Pharma Spend (USD B)"

def create_map_chart(filtered_data, spend_metric, spend_metric_label):
    """
    Creates a choropleth map chart using Plotly Express.

    This function generates a geographic map visualization where regions are 
    color-coded based on the specified spending metric. The colors represent 
    different values of the chosen metric, with a continuous color scale.

    Parameters:
    -----------
    filtered_data : GeoDataFrame or DataFrame
        The filtered dataset containing geographical and spend metric information. 
        Must include a geometry column that supports the `__geo_interface__` property.
    
    spend_metric : str
        The column name representing the spend metric used for coloring the map.

    spend_metric_label : str
        The display label for the spend metric in the color legend.

    Returns:
    --------
    plotly.graph_objects.Figure
        A Plotly choropleth map visualization.
    """

    tooltip_format, value_suffix = tooltip_formatter(spend_metric_label)

    map_chart = px.choropleth(filtered_data, 
              geojson=filtered_data.__geo_interface__, 
              locations='LOCATION',
              featureidkey = 'properties.LOCATION',  
              color=spend_metric,
              hover_data = {'name' : True, spend_metric: ':.2f', 'LOCATION': False},
              color_continuous_scale="tealrose"
            )
    
    map_chart.update_coloraxes(reversescale=True)
    map_chart.update_layout(
        autosize=True,
        coloraxis_colorbar=dict(title=spend_metric_label,
                                thickness=10,
                                len=0.5,
                                x=1),
        margin=dict(l=0, r=0, t=10, b=0)
    )
    
    map_chart.update_geos(showframe=False, lataxis=dict(range=[-60, 90]))
    return map_chart

def create_time_chart(filtered_data, spend_metric, spend_metric_label, start_year_select, end_year_select):
    """
    Creates a time series chart using Altair.

    This function generates a line chart with circular markers to visualize 
    trends over time for a given spending metric across different countries. 

    Parameters:
    -----------
    filtered_data : pandas.DataFrame
        The filtered dataset containing time-series data with columns for time, 
        spend metric, and country names.

    spend_metric : str
        The column name representing the spend metric used for the y-axis.

    spend_metric_label : str
        The display label for the spend metric in the chart.

    start_year_select : int
        The starting year for the time range filter.

    end_year_select : int
        The ending year for the time range filter.

    Returns:
    --------
    altair.Chart
        An Altair layered chart consisting of a line chart and point markers 
        for time-series visualization.
    """

    tooltip_format, value_suffix = tooltip_formatter(spend_metric_label)

    line = alt.Chart(filtered_data, width='container').mark_line().encode(
        x=alt.X('TIME:Q', title="Year").axis(format="d"),
        y=alt.Y(spend_metric, title=f"{spend_metric_label}"),
        color=alt.Color('name', legend=alt.Legend(title="Country"), scale=alt.Scale(scheme="dark2")),
        tooltip=['name', spend_metric]
    )

    points = alt.Chart(filtered_data).mark_circle().encode(
        x=alt.X('TIME:Q'),
        y=alt.Y(spend_metric),
        color='name', 
        tooltip=[
            alt.Tooltip('name:N', title="Country"),
            alt.Tooltip(spend_metric, title=spend_metric_label, format=tooltip_format)
        ]
    )

    timeseries_chart = (line + points).properties(
        usermeta={"embedOptions": {"actions": False}}
    )
    
    return timeseries_chart

def create_bar_chart(avg_data, spend_metric, spend_metric_label):
    """
    Creates a bar chart using Altair.

    This function generates a horizontal bar chart displaying the average value 
    of the specified spending metric across different countries.

    Parameters:
    -----------
    avg_data : pandas.DataFrame
        The dataset containing country names and the aggregated spend metric values.

    spend_metric : str
        The column name representing the spend metric used for the x-axis.

    spend_metric_label : str
        The display label for the spend metric in the chart.

    Returns:
    --------
    altair.Chart
        An Altair bar chart visualizing the average spend metric per country.
    """ 

    tooltip_format, value_suffix = tooltip_formatter(spend_metric_label)

    bar_chart = alt.Chart(avg_data, width='container', height=305).mark_bar(color="teal").encode(
        x=alt.X(f'mean({spend_metric}):Q', title=spend_metric_label),
        y=alt.Y('name:N', title="Country", sort='x'),  
        tooltip=[
            alt.Tooltip('name:N', title="Country"),
            alt.Tooltip(f'mean({spend_metric}):Q', title=spend_metric_label, format=tooltip_format)
        ]
    ).properties(
        usermeta={"embedOptions": {"actions": False}}
    )
    
    return bar_chart

def charts_callback(data, cache):
    @callback(
        Output('map_chart', 'figure'),
        Output('timeseries_chart', 'spec'),
        Output('bar_chart', 'spec'),
        Output('map_title', 'children'),
        Output('timeseries_title', 'children'),
        Output('bar_title', 'children'),
        Input('country_select', 'value'),
        Input('start_year_select', 'value'),
        Input('end_year_select', 'value'),
        Input('spend_metric', 'value'),
        Input('spend_metric', 'options')
    )
    @cache.memoize()  # Cache this function's results
    def create_chart(country_select, start_year_select, end_year_select, spend_metric, spend_metric_options):

        """
        Registers a Dash callback function to generate and update three charts 
        (map, time series, and bar chart) based on user-selected filters.

        This function defines an inner function `create_chart`, which processes 
        the input data by filtering it according to user selections and then 
        generates visualizations using Altair and Plotly.

        Parameters:
        -----------
        data : pandas.DataFrame
            The dataset containing country-wise spending data with columns such as 
            'name' (country), 'TIME' (year), and various spending metrics.

        cache : flask_caching.Cache
            A caching object to store memoized results for performance optimization.

        Returns:
        --------
        callback function
            A Dash callback function that updates:
            - A choropleth map (`figure`)
            - A time series chart (`spec`)
            - A bar chart (`spec`)
            - Titles for each chart (`children`)
        """

        # Filter data by countries and years
        filtered_data = data[
            data['name'].isin(country_select) &  # Filter by selected countries
            data['TIME'].between(start_year_select, end_year_select)  # Filter TIME between years
        ]
        # Get average data group by country and year
        avg_data = filtered_data.groupby('name')[spend_metric].mean().reset_index()
        spend_metric_label = next(item['label'] for item in spend_metric_options if item['value'] == spend_metric)
        print("Finish filtering data!")

        # More efficient for large data sets
        alt.data_transformers.enable('vegafusion')

        # Map Plot (Daria)
        map_title = f'{title_formatter(spend_metric_label)} by Country'
        map_chart = create_map_chart(filtered_data, 
                                    spend_metric, 
                                    spend_metric_label)

        # Time Series Chart (Jason)
        timeseries_title = f'{title_formatter(spend_metric_label)} by Country ({start_year_select} to {end_year_select})'
        timeseries_chart = create_time_chart(
            filtered_data, 
            spend_metric, 
            spend_metric_label, 
            start_year_select, 
            end_year_select
        )

        # Bar Chart (Celine)
        bar_title = f'Average {title_formatter(spend_metric_label)} by Country'
        bar_chart = create_bar_chart(
            avg_data, 
            spend_metric, 
            spend_metric_label
        )

        return map_chart, timeseries_chart.to_dict(format="vega"), bar_chart.to_dict(format="vega"), map_title, timeseries_title, bar_title