from dash import Input, Output, callback

@callback(
    Output('country_select', 'value'),
    Output('warning', 'children'),
    Input('country_select', 'value')
)
def limit_country_selection(selected_countries):
    """
    Limits the number of selected countries to a maximum of 10.

    Parameters
    ----------
    selected_countries : list of str
        The list of selected countries.

    Returns
    -------
    tuple
        A tuple containing:
        - list of str: The updated list of selected countries, limited to 10 if necessary.
        - str: A warning message if the selection exceeds 10 countries, otherwise an empty string.
    """
    if len(selected_countries) > 10:
        return selected_countries[:10], "Maximum 10 countries allowed. Extra selections have been removed."
    return selected_countries, ""  # Empty string removes the warning