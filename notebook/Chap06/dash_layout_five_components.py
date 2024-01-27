import dash
from dash import dcc
import dash_daq as daq
from dash import html
import plotly.express as px

# スタイルの作成
div_style={
    "width": "40%",
    "margin": "5%",
    "display": "inline-block",
    "verticalAlign": "top",
    "textAlign": "center",
}

div_style2={
    "width": "29%",
    "margin": "2%",
    "display": "inline-block",
    "verticalAlign": "top",
}

# スタイルシートの読み込み
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# レイアウトの作成
# Divのchildren属性に渡すレイアウト（左上）
top_left = html.Div(
    [
        html.H1("Dashアプリケーション"),
        dcc.Markdown(
            """
            5つのDivクラスの領域に、複数のコンポーネントを並べました。

            - 左上はH1、Markdown、右上はGraph
            - 左下はH3、Dropdown、Slider、真ん中下はH3, TextArea、右下はH3、Checklist、RadioItems

            上記のコンポーネントをDivのchildren属性に渡しました。
            """,
            style={
                "fontSize": 20,
                "textAlign": "left",
                "backgroundColor": "lightgrey",
                "padding": "3%",
            },
        ),

    ],
    style=div_style,
)

# グラフの作成
fig = px.line(
    x=[1,2,3,4,5],
    y=[[3,2,4,1,5],[2,4,3,5,3]],
    title="Dash Graph",
)
fig.data[0].name = "東京"
fig.data[1].name = "大阪"

# Divのchildren属性に渡すレイアウト（右上）
top_right = html.Div(
    [
        dcc.Graph(
            figure=fig
        )
    ],
    style=div_style,
)

# Divのchildren属性に渡すレイアウト（左下）
bottom_left = html.Div(
    [
        html.H3("ドロップダウン"),
        dcc.Dropdown(
            options=[
                {"label": "東京", "value": "東京"},
                {"label": "大阪", "value": "大阪"},
            ],
            value="大阪",
        ),
        html.H3("スライダ"),
        dcc.Slider(min=-10, max=10, marks={i: f"label{i}" for i in range(-10, 11, 5)}),
    ],
    style=div_style2,
)

# Divのchildren属性に渡すレイアウト（中央下）
bottom_mid = html.Div(
    [
        html.H3("テキストエリア入力"),
        html.Textarea(style={"height": 200, "width": "60%"}),
        html.Button("ボタン")
    ],
    style=div_style2,
)

# Divのchildren属性に渡すレイアウト（右下）
bottom_right = html.Div(
    [
        html.H3("選択肢", style={"textAlign": "center"}),
        # 2つのコンポーネントをスタイルシートを活用して横並びに
        dcc.Checklist(
            options=[
                {"label": "北海道", "value": "北海道"},
                {"label": "秋田", "value": "秋田"},
                {"label": "新潟", "value": "新潟"},
            ],
            value=["北海道", "新潟"],
            className="five columns",
        ),
        dcc.RadioItems(
            options=[
                {"label": "福岡", "value": "福岡"},
                {"label": "宮崎", "value": "宮崎"},
                {"label": "鹿児島", "value": "鹿児島"},
            ],
            value="鹿児島",
            className="five columns",
        ),
    ],
    style=div_style2,
)

app.layout = html.Div(
    children=[
        html.Div([top_left, top_right]),
        html.Div([bottom_left, bottom_mid, bottom_right]),
    ]
)

if __name__=="__main__":
    app.run_server(debug=True)