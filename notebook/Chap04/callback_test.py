import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

gapminder = plotly.data.gapminder()

# 引数にfigureを渡す
subplots_fig = go.FigureWidget(make_subplots(rows=1, cols=2, horizontal_spacing=0.15))
subplots_fig.add_trace(
    go.Scatter(
        x=gapminder["gdpPercap"],
        y=gapminder["lifeExp"],
        text=gapminder["country"],
        mode="markers",
        name="散布図",
    ),
    row=1,
    col=1,
)
subplots_fig.add_trace(
    go.Scatter(name="時系列データ",), row=1, col=2)

trace0, trace1 = subplots_fig.data
title_text="1人当たりGDPと平均寿命の散布図（左図）と平均寿命の時系列データ（右図）"
subplots_fig.update_layout(title={"text": title_text})
# 軸ラベル
subplots_fig.update_xaxes(title="1人当たりGDP", type="log", row=1, col=1)
subplots_fig.update_xaxes(title="年", type="log", row=1, col=2)
subplots_fig.update_yaxes(title="平均寿命")

def update_line(trace, points, selector):
    n = points.point_inds[0]
    country = gapminder.iloc[n, 0] # インデックスから国名を取得
    # 国名からデータを抽出
    country_df = gapminder.loc[gapminder["country"] == country].sort_values(
        "year"
    )
    trace1.x = country_df["year"]
    trace1.y = country_df["lifeExp"]
    subplots_fig.update_layout(
        annotations=[
            {
                "x": 1,
                "y": 1.1,
                "showarrow": False,
                "text": country,
                "xref": "paper",
                "yref": "paper",
            }
        ]
    )
    
trace0.on_click(update_line)
# このままだとfigがブラウザに行かない
# subplots_fig
# こうするとコールバックが効かない
subplots_fig.show()
