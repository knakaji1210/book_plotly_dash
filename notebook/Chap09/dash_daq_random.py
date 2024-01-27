import dash
from dash import dcc
from dash import html
import dash_daq as daq
from dash.dependencies import Input, Output
import numpy as np

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

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
        # 計器を並べる
        html.Div(
            [
                html.Div(
                    [html.H2("ゲージ"), daq.Gauge(id="gauge1")],
                    className="three columns",
                ),
                html.Div(
                    [html.H2("グラデュエートバー"), daq.GraduatedBar(id="gauge2")],
                    className="three columns",
                ),
                html.Div(
                    [html.H2("タンク"), daq.Tank(id="gauge3")],
                    className="three columns",
                ),
                html.Div(
                    [html.H2("LEDディスプレイ"), daq.LEDDisplay(id="gauge4")],
                    className="three columns",
                ),
            ],
            style={"margin": "auto"},
        ),
    ]
)

# オンとオフを管理する
@app.callback(
    Output("daq-interval", "disabled"),
    Input("daq-powerbutton", "on")
)
def gauge_witch(buttonon):
    if buttonon:
        return False
    else:
        return True

# 計器にランダムな値を返す
@app.callback(
    Output("gauge1", "value"),
    Output("gauge2", "value"),
    Output("gauge3", "value"),
    Output("gauge4", "value"),
    Input("daq-interval", "n_intervals")
)
def update_gauges(n_intervals):
    return list(np.random.uniform(0,10,4))

if __name__=="__main__":
    app.run_server(debug=True)