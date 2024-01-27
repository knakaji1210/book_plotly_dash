import dash
from dash import html

# 1行目用CSS辞書
div_style3={
    "width": "40%",
    "height": "250px",
    "backgroundColor": "lime",
    "margin": "5%",
    "display": "inline-block",
}

# 2行目用CSS辞書
div_style4={
    "width": "29%",
    "height": "250px",
    "backgroundColor": "skyblue",
    "margin": "2%",
    "display": "inline-block",
}

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # 1行目　2つの長方形
        html.Div(
            [html.Div(style=div_style3), html.Div(style=div_style3)],
            id="first_leader",
        ),
        # 2行目　3つの長方形
        html.Div(
            [
                html.Div(style=div_style4), 
                html.Div(style=div_style4),
                html.Div(style=div_style4)
            ],
            id="second_leader",
        ),
    ],
    id="leader"
)

if __name__=="__main__":
    app.run_server(debug=True)