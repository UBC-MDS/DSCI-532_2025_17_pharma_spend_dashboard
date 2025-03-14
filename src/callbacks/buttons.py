from dash import Input, Output, callback, State

@callback(
    Output("collapse", "is_open"),
    Input("collapse-button", "n_clicks"),
    State("collapse", "is_open"),  # Pass the current "state" of the component (is it open or not)
)
def toggle_collapse(n, is_open):
    """
    Toggles the state of a collapsible component in a Dash app.

    Parameters
    ----------
    n : int
        The number of times the toggle button has been clicked.
    is_open : bool
        The current state of the collapsible component (True if open, False if closed).

    Returns
    -------
    bool
        The new state of the collapsible component. It toggles if the button has been clicked
        at least once; otherwise, it remains unchanged.
    """
    # print(n)  # The number of times the button has been clicked
    # print(is_open)  # Whether the collapse is open or not
    return not is_open if n else is_open