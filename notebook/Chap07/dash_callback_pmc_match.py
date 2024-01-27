import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

# データの読み込み
gapminder = px.data.gapminder()

# 横に2つのコンポーネントを並べるためのスタイル
half_style = {"width": "50%", "display": "inline-block"}

app = dash.Dash(__name__)

# 2つのコンポーネントをもつレイアウト
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop", n_clicks=0),  # 新たなドロップダウンを追加するボタン
        html.Div(id="my_div", children=[]),  # ドロップダウンを追加するDiv
    ]
)

# コールバック1
@app.callback(
    Output("my_div", "children"),
    Input("add_drop", "n_clicks"),
    State("my_div", "children"),
    prevent_initial_call=True,
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            ), 
            dcc.Dropdown(
                id={"type": "my_dropdown2", "index": n_clicks},
                options=[
                    {"label": col, "value": col} for col in gapminder.columns[3:6]
                ],
                value="lifeExp",
            ),
            dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
        ],
        style=half_style,
    )
    children.append(new_layout)
    return children

# コールバック2
@app.callback(
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),
    Input({"type": "my_dropdown2", "index": MATCH}, "value"),
)
def update_graph(selected_value, selected_col):
    gap = gapminder[gapminder["country"] == selected_value]
    return px.line(gap, x="year", y=selected_col)

if __name__=="__main__":
    app.run_server(debug=True)