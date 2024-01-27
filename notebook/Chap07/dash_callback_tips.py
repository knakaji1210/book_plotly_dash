import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# データの読み込み
tips = px.data.tips()

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)


# レイアウトの作成
app.layout = html.Div(
    [
        # 指定したグラフに応じてグラフのタイトルを変更
        html.H3(id="title", style={"textAlign": "center"}),
        html.Div(
            [
                html.Div(
                    [
                        html.H4("曜日選択"),
                        # 曜日選択のドロップダウンの作成
                        dcc.Dropdown(
                            id="day_selector",
                            options=[
                                {"value": dow, "label": dow} for dow in tips.day.unique()
                            ],
                            multi=True,
                            value=["Thur", "Fri", "Sat", "Sun"],
                        ),
                    ],
                    className="six columns",
                ),
                html.Div(
                    [
                        html.H4("グラフ選択"),
                        # グラフ選択のドロップダウンの作成
                        dcc.Dropdown(
                            id="graph_selector",
                            options=[
                                {"value": "bar", "label": "bar"},
                                {"value": "scatter", "label": "scatter"},
                            ],
                            value="bar",
                        ),
                    ],
                    className="six columns",
                ),
            ],
            style={"padding": "2%", "margin": "auto"},
        ),
        # グラフの表示場所
        html.Div(
            [
                dcc.Graph(id="app_graph", style={"padding": "3%"}),
            ],
            style={"padding": "3%", "marginTop": 50},
        ),    ]
)

# コールバックの作成
@app.callback(
    Output("title", "children"),
    Output("app_graph", "figure"),
    Input("day_selector", "value"),
    Input("graph_selector", "value"),
)

# コールバック関数
def update_graph(selected_days, selected_graph):
    # データフレームの作成
    selected_df = tips[tips["day"].isin(selected_days)]
    # 選択されたグラフの種類により、タイトル表示データとグラフを作成
    if selected_graph == "scatter":
        title = "テーブルごとデータ（散布図）"
        figure = px.scatter(
            selected_df, x="total_bill", y="tip", color="smoker", height=600
        )
    else:
        title = "曜日ごと売上（棒グラフ）"
        figure = px.bar(
            selected_df, x="day", y="total_bill", height=600
        )
    return title, figure

if __name__=="__main__":
    app.run_server(debug=True)