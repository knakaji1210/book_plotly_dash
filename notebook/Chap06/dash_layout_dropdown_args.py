import dash  
# import dash_core_components as dcc
# これがdeprecatedということらしく
from dash import dcc
# これに置き換えた

# Dashインスタンスを生成する
app = dash.Dash(__name__)

app.layout = dcc.Dropdown(
    options=[ #　選択肢の設定
        {"label": "赤", "value": "red"},
        {"label": "黄", "value": "yellow"},
        {"label": "青", "value": "blue"},
    ],
    value="red", # 初期値の設定
    clearable=False, # 選択を削除できないように設定
    style={"textAlign": "center"}, # 文字を中央に寄せる
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)