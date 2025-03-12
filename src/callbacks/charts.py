from dash import Input, Output, callback
import plotly.express as px
import altair as alt

def create_map_chart(filtered_data, spend_metric, spend_metric_label):
    """
    Creates a map chart
    """
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
        tooltip=[
            alt.Tooltip('name:N', title="Country"),
            alt.Tooltip(spend_metric, title=spend_metric_label, format='$,.2f')
        ]
    )

    timeseries_chart = (line + points).properties(
        usermeta={"embedOptions": {"actions": False}}
    )
    
    return timeseries_chart

def create_bar_chart(avg_data, spend_metric, spend_metric_label):
    """
    Creates a bar chart
    """    
    bar_chart = alt.Chart(avg_data, width='container', height=305).mark_bar(color="teal").encode(
        x=alt.X(f'mean({spend_metric}):Q', title="Total Spend (USD)"),
        y=alt.Y('name:N', title="Country", sort='x'),  
        tooltip=[
            alt.Tooltip('name:N', title="Country"),
            alt.Tooltip(f'mean({spend_metric}):Q', title=spend_metric_label, format='$,.2f')
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
        map_title = f'{spend_metric_label} by Country'
        map_chart = create_map_chart(filtered_data, 
                                    spend_metric, 
                                    spend_metric_label)

        # Time Series Chart (Jason)
        timeseries_title = f'{spend_metric_label} by Country ({start_year_select} to {end_year_select})'
        timeseries_chart = create_time_chart(
            filtered_data, 
            spend_metric, 
            spend_metric_label, 
            start_year_select, 
            end_year_select
        )

        # Bar Chart (Celine)
        bar_title = f'Average {spend_metric_label} by Country'
        bar_chart = create_bar_chart(
            avg_data, 
            spend_metric, 
            spend_metric_label
        )

        return map_chart, timeseries_chart.to_dict(format="vega"), bar_chart.to_dict(format="vega"),map_title, timeseries_title, bar_title