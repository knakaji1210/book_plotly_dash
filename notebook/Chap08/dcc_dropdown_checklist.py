import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # Checklistの作成
        dcc.Checklist(
            # 選択肢の定義　"label"と"value"が必須
            options=[
                {"label": "東京", "value": "tokyo"},
                {"label": "北海道", "value": "hokkaido"},
                {"label": "静岡", "value": "shizuoka"},
                {"label": "愛知", "value": "aichi"},
                {"label": "京都", "value": "kyoto"},
            ],
            # 初期値を京都に設定
            value=["hokkaido", "kyoto"], # valueはリストに入れて渡す
            # 文字を中央に寄せる
            style={"textAlign": "center"},
        )
    ],
    style={"width": "80%", "margin": "auto"},
)

if __name__=="__main__":
    app.run_server(debug=True)