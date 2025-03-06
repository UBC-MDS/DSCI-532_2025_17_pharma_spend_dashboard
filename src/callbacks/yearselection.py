from dash import Input, Output, callback

def year_selection_callback(times):
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