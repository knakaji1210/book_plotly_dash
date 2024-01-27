import datetime

import dash
from dash import dcc
from dash import html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# 現在の時刻から5分前の時刻
start = pd.Timestamp(datetime.datetime.now()).round("s") - datetime.timedelta(
    seconds=300
)

df = pd.DataFrame(
    {"price": np.random.randn(1000).cumsum()},   # cumsumは累積和
    index=pd.date_range(start, freq="s", periods=1000),
)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # タイトルは現在の時刻とn_clickの属性を用いて作成する
        html.H1(id="realtime-title", style={"textAlign": "center"}),
        dcc.Graph(id="realtime-graph"),
        # Intervalクラスの引数intervalで更新間隔を設定・更新最大回数は100回
        dcc.Interval(id="realtime-interval", interval=1000, max_intervals=100),
    ]
)

# コールバック
@app.callback(
    Output("realtime-title", "children"),
    Output("realtime-graph", "figure"),
    Input("realtime-interval", "n_intervals"),
)
def update_graph(n_intervals):
    # 現時点から120秒前までのデータを取得し、グラフを返す
    now = pd.Timestamp(datetime.datetime.now()).round("s")
    past = now - datetime.timedelta(seconds=120)

    plot_df = df.loc[past:now]

    # タイトルとグラフを戻り値とする
    return (
        f"live-update-chart: {now} / n_intervals: {n_intervals}",
        {"data": [go.Scatter(x=plot_df.index, y=plot_df["price"])]},
    )

if __name__=="__main__":
    app.run_server(debug=True)