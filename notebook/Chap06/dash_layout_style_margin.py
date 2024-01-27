import dash  
from dash import html

app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    # スタイルの設定
    style={
        "fontSize": 50,
        "color": "white",
        "backgroundColor": "#000000",
        "width": 400,
        "margin": "auto",
    },
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)