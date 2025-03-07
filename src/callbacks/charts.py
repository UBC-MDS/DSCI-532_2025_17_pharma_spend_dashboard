from dash import Input, Output, callback
import altair as alt

def create_map_chart(world_countries, filtered_data_merged, spend_metric, spend_metric_label):
    """
    Creates a map chart
    """
    map = alt.Chart(world_countries, width=800).mark_geoshape(stroke='white', color='lightgrey').encode()   
    chart = map + alt.Chart(filtered_data_merged).mark_geoshape().encode(
        color = alt.Color(
            spend_metric,
            scale = alt.Scale(scheme='teals'),
            legend=alt.Legend(title=f'Average {spend_metric_label}')
        ),
        tooltip = 'name'
    ).project(
        'naturalEarth1'
    )
    
    bubbles = alt.Chart(filtered_data_merged).transform_calculate(
        centroid=alt.expr.geoCentroid(None, alt.datum)
    ).mark_circle(
        stroke='brown',
        fill = 'brown',
        strokeWidth = 1,
        opacity = 0.8
    ).encode(
        longitude='centroid[0]:Q',
        latitude='centroid[1]:Q',
        size=alt.Size(spend_metric, 
                  legend=alt.Legend(title=None)),
        tooltip = alt.Tooltip(spend_metric, format=".0f")
    )
    map_chart = chart + bubbles

    return map_chart

def create_time_chart(filtered_data, spend_metric, spend_metric_label, start_year_select, end_year_select):
    """
    Creates a time series chart
    """
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
        tooltip=['name', spend_metric]
    )

    timeseries_chart = (line + points).properties(
        title= f'{spend_metric_label} by Country ({start_year_select} to {end_year_select})'
    )
    return timeseries_chart

def create_bar_chart(avg_data, spend_metric, spend_metric_label):
    """
    Creates a bar chart
    """    
    bar_chart = alt.Chart(avg_data, width='container', height=300).mark_bar(color="teal").encode(
        x=alt.X(f'mean({spend_metric}):Q', title="Total Spend (USD)"),
        y=alt.Y('name:N', title="Country", sort='x'),  
        tooltip=['name', f'mean({spend_metric})']
    ).properties(
        title=f"Average {spend_metric_label} by Country"
    )
    return bar_chart

def charts_callback(data, world_countries):
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
        # map = alt.Chart(world_countries, width=800).mark_geoshape(stroke='white', color='lightgrey').encode()
        map_chart = create_map_chart(
            world_countries, 
            filtered_data, 
            spend_metric, 
            spend_metric_label
        )

        # Time Series Chart (Jason)
        timeseries_chart = create_time_chart(
            filtered_data, 
            spend_metric, 
            spend_metric_label, 
            start_year_select, 
            end_year_select
        )

        # Bar Chart (Celine)
        bar_chart = create_bar_chart(
            avg_data, 
            spend_metric, 
            spend_metric_label
        )

        return map_chart.to_dict(format="vega"), timeseries_chart.to_dict(format="vega"), bar_chart.to_dict(format="vega")