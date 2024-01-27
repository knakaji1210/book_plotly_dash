import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


# レイアウト
app.layout = html.Div(
    [
        html.H1(id="callback-output"),
        # 引数updatemodeに"drag"を渡し、動作を即座に反映するように設定
        dcc.Slider(
            id="callback-input",
            min=0,
            max=100, 
            value=0,
            updatemode="drag",
        ),
    ],
    style={"textAlign": "center", "width": "60%", "margin": "auto"},
)

# コールバック
@app.callback(
    Output("callback-output", "children"),  # 出力項目
    Input("callback-input", "value"),    # 入力項目
)

# コールバック関数
def update_app(num_value):
    return num_value

if __name__=="__main__":
    app.run_server(debug=True)