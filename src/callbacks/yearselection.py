from dash import Input, Output, callback

def year_selection_callback(times):
    """
    Creates a callback to update the available options for the end year selection
    based on the selected start year.

    Parameters
    ----------
    times : list of int
        A list of available years.

    Returns
    -------
    tuple
        A tuple containing:
        - A list of dictionaries representing the available end year options,
          where each dictionary has 'label' and 'value' keys.
        - The selected end year value, ensuring it remains valid.
    """
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