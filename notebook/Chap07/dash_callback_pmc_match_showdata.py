import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

# データの読み込み
gapminder = px.data.gapminder()

app = dash.Dash(__name__)

# レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop"),  # 新たなドロップダウンを追加するボタン
        html.Div(id="show_drop", children=[]),  # ドロップダウンを追加するDiv
    ],
    style={"width": "80%", "margin": "2% auto"},
)

# コールバック1
@app.callback(
    Output("show_drop", "children"),
    Input("add_drop", "n_clicks"),
    State("show_drop", "children"),
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
            # 文字列を表示するコンポーネント
            html.P(id={"type": "text_show", "index": n_clicks}),
        ]
    )
    children.append(new_layout)
    return children

# コールバック2
@app.callback(
    Output({"type": "text_show", "index": MATCH}, "children"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),
)
def update_graph(selected_values):
    return str(selected_values)

if __name__=="__main__":
    app.run_server(debug=True)