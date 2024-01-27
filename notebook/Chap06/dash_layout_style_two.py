import dash  
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P(
            "こんにちは。昨日は雪が降りました。",
            style={
                "fontSize": 50,
                "color": "white",
                "backgroundColor": "black",
                "width": "40%",
                "display": "inline-block",
            }
        ),
        html.P(
            "こんにちは。今日は晴れました。",
            style={
                "fontSize": 50,
                "color": "white",
                "backgroundColor": "red",
                "width": "40%",
                "display": "inline-block",
                "verticalAlign": "top",
            }
        ),
    ]
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)