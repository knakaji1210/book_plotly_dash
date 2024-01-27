import dash
from dash import dcc
from dash import html
import plotly
import plotly.express as px

gapminder = plotly.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # ドロップダウンの作成
        dcc.Dropdown(
            id="gapminder-dropdown",
            # country列から一意なデータを抽出して選択肢を作成
            options=[
                {"label": c, "value": c} for c in gapminder["country"].unique()
            ],
            # 複数国をリストに入れ初期値を設定
            value=["Japan", "China", "United States"],
            # 複数選択を有効化
            multi=True,
            # 文字を中央に寄せる
            style={"textAlign": "center"},
        )
    ],
    style={"width": "50%", "margin": "auto"},
)

if __name__=="__main__":
    app.run_server(debug=True)