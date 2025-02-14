from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("Global Pharmaceuitical Spendings"),
                width=12
            )
        ),
        
        dbc.Row(
            [   
                dbc.Col(
                    
                    html.Div(["Global filters go here"]),
                    width=4 
                ),
                
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.Div("Local filters go here"), width=12)
                            ]
                        ),
                        
                        dbc.Row(
                            [
                                dbc.Col(html.Div("Graph 1"), width=6),
                                dbc.Col(html.Div("Graph 2"), width=6),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.Div("Graph 3"), width=6),
                                dbc.Col(html.Div("Graph 4"), width=6),
                            ]
                        )
                    ],
                    width=8
                ),
            ]
        )
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run(debug=True)