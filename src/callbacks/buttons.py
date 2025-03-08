from dash import Input, Output, callback, State

@callback(
    Output("collapse", "is_open"),
    Input("collapse-button", "n_clicks"),
    State("collapse", "is_open"),  # Pass the current "state" of the component (is it open or not)
)
def toggle_collapse(n, is_open):
    print(n)  # The number of times the button has been clicked
    print(is_open)  # Whether the collapse is open or not
    return not is_open if n else is_open