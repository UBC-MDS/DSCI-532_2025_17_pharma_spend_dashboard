from dash import Input, Output, callback
import dash

@callback(
    Output('country_select', 'value'),
    Output('warning', 'children'),
    Output('warning_timer', 'n_intervals'),  # Reset timer when warning appears
    Input('country_select', 'value'),
    Input('warning_timer', 'n_intervals')  # Listen for timer expiration
)
def limit_country_selection(selected_countries, n_intervals):
    """
    Limits the number of selected countries to a maximum of 10 and ensures at least one country is selected.
    Automatically clears the warning message after a few seconds.

    Parameters
    ----------
    selected_countries : list of str
        The list of selected countries.
    n_intervals : int
        The number of intervals triggered by the warning timer. Used to clear the warning message after a delay.

    Returns
    -------
    tuple
        A tuple containing:
        - list of str: The updated list of selected countries, ensuring at least one is selected and limiting to 10.
        - str: A warning message if selection is invalid (too few or too many countries), otherwise an empty string.
        - int: Resets the warning timer when a message is shown and clears it when the timer expires.
    """
    ctx = dash.callback_context  # Get which input triggered callback
    if not ctx.triggered:
        return selected_countries, "", 0

    triggered_input = ctx.triggered[0]['prop_id'].split('.')[0]

    # If the timer expired, clear the warning
    if triggered_input == "warning_timer":
        return selected_countries, "", 0

    # Validate country selection
    if len(selected_countries) == 0:
        return ['Canada'], "At least one country needs to be selected.", 0
    if len(selected_countries) > 10:
        return selected_countries[:10], "Maximum 10 countries allowed. Extra selections have been removed.", 0

    return selected_countries, "", 0  # Default return