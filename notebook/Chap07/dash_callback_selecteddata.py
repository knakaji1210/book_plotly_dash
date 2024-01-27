import json

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# データの作成
gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_stylesheets=dash_stylesheets,
)

# アプリケーションのレイアウト
app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        # 散布図の作成
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, 
                x="gdpPercap", 
                y="lifeExp", 
                hover_name="country",
                # クリック＋shiftで複数データを選択
                template={"layout": {"clickmode": "event+select"}},
            ),
        ),
        # ホバーデータを表示するPコンポーネント
        html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)

# コールバック
@app.callback(
    Output("hoverdata-p", "children"),
    # GraphのselectedData属性を指定する
    Input("gapminder-g", "selectedData"),
)
def show_hover_data(selectedData):
        return json.dumps(selectedData)

if __name__=="__main__":
    app.run_server(debug=True)