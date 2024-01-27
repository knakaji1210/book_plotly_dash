import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # スライダの作成
        dcc.Slider(
            id="thisSlider",
            max=5,
            min=-1,       # 本にはなかったものを追加
            step=0.01,
            value=2,
            marks=None,   # 本にはなかったものを追加
            tooltip={"always_visible": False, "placement": "bottom"},
            updatemode="drag",
        ),
        html.P(
            id="pow-output", style={"marginTop": "5%", "fontSize": 30}
            # コールバックの返り値を受け取る
        ),
    ],
    style={"width": "80%","margin": "5% auto"},
)

# コールバック
@app.callback(
        Output("pow-output", "children"),
        Input("thisSlider", "value"),
)
def display_value(value):
    return f"数値：{value} | 10のべき乗：{10 ** value: .3f}"

if __name__=="__main__":
    app.run_server(debug=True)