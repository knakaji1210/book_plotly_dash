import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# データの読み込み
iris = px.data.iris()

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)

# レイアウト
app.layout = html.Div(
    [
        # URLを生成
        dcc.Location(id="my_location"),
        # コンテンツの表示
        html.Div(
            id="show_location1",
            style={"height": 600},
        ),
        html.Br(),
        # リンクの設置
        dcc.Link("home", href="/"),
        html.Br(),
        dcc.Link("/graph", href="/graph"),
        html.Br(),
        dcc.Link("/table", href="/table"), 
    ],
    style={"textAlign": "center"},
)

# ページごとのコンテンツの作成
# home(/)ページ作成
home = html.H1("irisデータ")

# graph(/graph)ページ作成
graph = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("X軸: "),
                        dcc.RadioItems(
                            id="x_axis_radio",
                            options=[
                                {"label": col, "value": col} for col in iris.columns[:4]
                            ],
                            value="sepal_width",
                        ),
                    ],
                    style={"display": "inline-block"},
                ),
                html.Div(
                    [
                        html.P("Y軸: "),
                        dcc.RadioItems(
                            id="y_axis_radio",
                            options=[
                                {"label": col, "value": col} for col in iris.columns[:4]
                            ],
                            value="sepal_length",
                        ),
                    ],
                    style={"display": "inline-block"},
                ),
            ]
        ),
        dcc.Graph(id="radio-graph"),        
    ]
)

# table(/table)ページ作成
table = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="species-dropdown",
                    options=[{"value": col, "label": col} for col in iris.columns],
                    multi=True,
                    value=["sepal_length", "sepal_width"],
                )
            ],
            style={"width": "60%", "margin": "auto"},
        ),
        dcc.Graph(id="table"),
    ]
)

# ページ切り替え用コールバック
@app.callback(
    Output("show_location1", "children"),
    Input("my_location", "pathname"),
)
def update_location(pathname):
    if pathname == "/graph":
        return graph
    elif pathname == "/table":
        return table
    else:
        # 条件にないpathnameはhomeを返す
        return home

# グラフ更新用コールバック
@app.callback(
    Output("radio-graph", "figure"),
    Input("x_axis_radio", "value"),
    Input("y_axis_radio", "value"),
)
def update_graph(selected_x, selected_y):
    return px.scatter(
        iris,
        x=selected_x,
        y=selected_y,
        color="species",
        marginal_y="violin",
        marginal_x="box",
        title="irisグラフ",
    )

# テーブル更新用コールバック
@app.callback(
    Output("table", "figure"), 
    Input("species-dropdown", "value")
)
def update_table(selected_value):
    iris_df = iris[selected_value]
    return go.Figure(
        data=go.Table(
            header={"values": iris_df.columns},
            cells={"values": [iris_df[col].tolist() for col in iris_df.columns]},
        ),
        layout=go.Layout(title="irisデータテーブル"),
    )

if __name__=="__main__":
    app.run_server(debug=True)