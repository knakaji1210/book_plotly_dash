import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("5つの四角形を並べたアプリケーション"),
        html.Div(
            [
                html.Div(className="roundsqlime colmuns"),
                html.Div(className="roundsqlime colmuns"),
            ]
        ),
        html.Div(
            [
                html.Div(className="roundsqblue colmuns"), 
                html.Div(className="roundsqblue colmuns"),
                html.Div(className="roundsqblue colmuns"),
            ]
        ),
    ]
)

if __name__=="__main__":
    app.run_server(debug=True)