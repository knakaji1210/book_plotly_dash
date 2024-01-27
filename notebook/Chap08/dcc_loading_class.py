import time

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

app.layout = html.Div(
    [
        html.H3("Loading_Test"),
        dcc.Textarea(id="input_text", value="最初の値"),
        html.Button(id="input_1", children="Push"),
        # コールバックの出力先のDivを管理するLoadingコンポーネントを設定する
        dcc.Loading(
            id="loading_1",
            type="circle",
            children=[html.H1(id="loading", style={"margin": 100})],
        ),
    ],
    style={"textAlign": "center"},
)

# コールバック
@app.callback(
        Output("loading", "children"),
        Input("input_1", "n_clicks"),
        State("input_text", "value"),
)
def input_trigger_spinner(n_clicks, value):
    time.sleep(3)
    return value

if __name__=="__main__":
    app.run_server(debug=True)