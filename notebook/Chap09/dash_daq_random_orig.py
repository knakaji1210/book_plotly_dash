import dash
from dash import dcc
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output
import numpy as np

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ➊ レイアウト
app.layout = html.Div(
    [
        html.Div(
            [
                daq.PowerButton(
                    id="daq-powerbutton",
                    label="計器を動作させるボタン",
                    on=False,
                    size=100,
                    color="red",
                ),
                dcc.Interval(id="daq-interval", interval=1000, n_intervals=0),
            ]
        ),
        # ➍ 計器を並べる
        html.Div(
            [
                html.Div(
                    [html.H2("ゲージ"), daq.Gauge(id="guage1")], className="three columns",
                ),
                html.Div(
                    [html.H2("ゲージ"), daq.Gauge(id="guage2")], className="three columns",
                )
            ],
            style={"margin": "auto"},
        ),
    ]
)

# ➋ コールバック オンとオフを管理するコールバック
@app.callback(Output("daq-interval", "disabled"), Input("daq-powerbutton", "on"))
def guage_witch(buttonon):
    if buttonon:
        return False
    else:
        return True


# ➌ コールバック 計器にランダムな値を返すコールバック
@app.callback(
    Output("guage1", "value"),
    Output("guage2", "value"),
    Input("daq-interval", "n_intervals"),
)
def update_guages(n_intervals):
    return list(np.random.uniform(0, 10, 2))


if __name__ == "__main__":
    app.run_server(debug=True)
