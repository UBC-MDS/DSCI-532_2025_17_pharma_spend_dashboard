from dash import Input, Output, callback, State

def summary_callback(data, cache):
    """
    Defines a callback function to display dahsboard components

    Parameters
    ----------
    data : geopandas.DataFrame
        The dataset containing country-level economic and healthcare expenditure data.
    cache : object
        A caching mechanism to store and retrieve computed results efficiently.

    Returns
    -------
    function
        A memoized callback function that updates summary statistics and growth metrics
        based on user-selected inputs.
    """
    @callback(
        Output("gdp-value", "children"),
        Output("health-value", "children"),
        Output("capita-value", "children"),
        Output("total-value", "children"),
        Output("gdp-growth", "children"),
        Output("gdp-growth", "style"),
        Output("health-growth", "children"),
        Output("health-growth", "style"),
        Output("capita-growth", "children"),
        Output("capita-growth", "style"),
        Output("total-growth", "children"),
        Output("total-growth", "style"),

        Input('submit_button', 'n_clicks'),
        State("country_select", "value"),
        State("start_year_select", "value"),
        State("end_year_select", "value"),
        State("spend_metric", "value"),
    ) 
    @cache.memoize()  # Cache this function's results
    
    def update_summary(n_clicks, countries, year_from, year_to, spend_metric):
        """
        Updates and returns summary statistics and growth metrics for selected countries
        and time periods based on the specified spending metric.

        Parameters
        ----------
        n_clicks : int or None
            The number of times the submit button has been clicked.
        countries : list of str
            The selected countries for which the summary statistics are calculated.
        year_from : int
            The starting year for filtering the dataset.
        year_to : int
            The ending year for filtering the dataset.
        spend_metric : str
            The selected spending metric, which can be:
            - "PC_GDP"
            - "PC_HEALTHXP"
            - "USD_CAP"
            - "TOTAL_SPEND"

        Returns
        -------
        tuple
            A tuple containing:
            - GDP percentage value (str)
            - Healthcare expenditure percentage value (str)
            - Per capita expenditure value (str)
            - Total spending value (str)
            - GDP growth value (str) and its corresponding style (dict)
            - Healthcare expenditure growth value (str) and its corresponding style (dict)
            - Per capita expenditure growth value (str) and its corresponding style (dict)
            - Total spending growth value (str) and its corresponding style (dict)
        """
        if n_clicks is None or n_clicks == 0:
            print("Loading default charts on first load...")

        filtered_data = data.query("name in @countries and @year_from <= TIME <= @year_to")

        if filtered_data.empty:
            return ["N/A"] * 8 + [{}] * 4  

        def calc_growth(metric):
            df = filtered_data.groupby("TIME")[metric].mean()
            growth = ((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100
            
            if growth > 0:
                return f"+{growth:.1f}% Growth", {"color": "green", "textAlign": "center", "marginBottom": "1px"}
            else:
                return f"{growth:.1f}% Growth", {"color": "red", "textAlign": "center", "marginBottom": "1px"}

        # Compute summary stats
        gdp_value = f"{filtered_data['PC_GDP'].mean():.2f}%"
        health_value = f"{filtered_data['PC_HEALTHXP'].mean():.2f}%"
        capita_value = f"${filtered_data['USD_CAP'].mean():,.2f}"
        total_value = f"${int(filtered_data['TOTAL_SPEND'].mean()):,}"
        
        gdp_growth, gdp_growth_style = calc_growth("PC_GDP")
        health_growth, health_growth_style = calc_growth("PC_HEALTHXP")
        capita_growth, capita_growth_style = calc_growth("USD_CAP")
        total_growth, total_growth_style = calc_growth("TOTAL_SPEND")

        return (gdp_value, health_value, capita_value, total_value,
                gdp_growth, gdp_growth_style,
                health_growth, health_growth_style,
                capita_growth, capita_growth_style,
                total_growth, total_growth_style)
            
@callback(
[
    Output("card-gdp", "style"),
    Output("card-health", "style"),
    Output("card-capita", "style"),
    Output("card-total", "style"),
],
Input("spend_metric", "value"),
)
def highlight_selected_card(spend_metric):
    """
    Highlights the selected spending metric card in the UI.

    Parameters
    ----------
    spend_metric : str
        The selected spending metric, which can be one of:
        - "PC_GDP"
        - "PC_HEALTHXP"
        - "USD_CAP"
        - "TOTAL_SPEND"

    Returns
    -------
    tuple of dict or None
        A tuple containing the style for each card. The selected metric receives a highlighted style,
        while others remain unchanged.
    """
    highlight_style = {
        "border": "3px solid #008080",  # Teal border "2px solid #808080"
        "borderRadius": "10px",
        "backgroundColor": "#e6e6e6" #Gray
    }

    return (
        highlight_style if spend_metric == "PC_GDP" else None,
        highlight_style if spend_metric == "PC_HEALTHXP" else None,
        highlight_style if spend_metric == "USD_CAP" else None,
        highlight_style if spend_metric == "TOTAL_SPEND" else None
        )