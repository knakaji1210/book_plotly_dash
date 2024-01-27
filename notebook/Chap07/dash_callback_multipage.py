import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# データの読み込み
iris = px.data.iris()

app = dash.Dash(__name__)

# レイアウト
app.layout = html.Div(
    [
        # URLを生成
        dcc.Location(id="my_location"),
        # コンテンツの表示
        html.Div(
            id="show_location",
            style={"fontSize": 30, "textAlign": "center", "height": 400},
        ),
        html.Br(),
        # リンクの設置
        dcc.Link("home", href="/"),
        html.Br(),
        dcc.Link("/graph", href="/graph"),
        html.Br(),
        dcc.Link("/table", href="/table"), 
    ],
    style={"fontSize": 30, "textAlign": "center"},
)

# ページごとのコンテンツの作成
# home(/)のコンテンツ
home = html.H1("Irisデータ")

# graph(/graph)のコンテンツ
graph = dcc.Graph(
    figure=px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title="Irisグラフ"
    )
)

# table(/table)のコンテンツ
table = dcc.Graph(
    figure=go.Figure(
        data=go.Table(
            header={"values": iris.columns},
            cells={"values": [iris[col].tolist() for col in iris.columns]},

        ),
        layout=go.Layout(title="Irisデータテーブル")
    )
)

@app.callback(
    Output("show_location", "children"),
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

if __name__=="__main__":
    app.run_server(debug=True)