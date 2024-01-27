import dash
from dash import html

# 1段目用CSS辞書
div_style3={
    "height": "250px",
    "backgroundColor": "lime",
    "margin": "5%",
}

# 2段目用CSS辞書
div_style4={
    "height": "250px",
    "backgroundColor": "skyblue",
    "margin": "1%",
}

# スタイルシートの読み込み
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H1("5つの四角形を並べたアプリケーション"),
        # 1段目　2つの長方形
        html.Div(
            [
                html.Div(style=div_style3, className="five columns"),
                html.Div(style=div_style3, className="five columns"),
            ],
            id="first_leader",
        ),
        # 2段目　3つの長方形
        html.Div(
            [
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
            ],
            id="second_leader",
        ),
    ],
    id="leader",
)

if __name__=="__main__":
    app.run_server(debug=True)