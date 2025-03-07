from dash import Input, Output, callback

@callback(
    Output('country_select', 'value'),
    Output('warning', 'children'),
    Input('country_select', 'value')
)
def limit_country_selection(selected_countries):
    # Allow maximum 10 countries to be selected
    if len(selected_countries) > 10:
        return selected_countries[:10], "Maximum 10 countries allowed. Extra selections have been removed."
    return selected_countries, ""  # Empty string removes the warning