import dash  
# import dash_html_components as html
# これがdeprecatedということらしく
from dash import html
# これに置き換えた

# Dashインスタンスを生成する
app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    # スタイルの設定
    style={
        "fontSize": 50,
        "color": "white",
        "backgroundColor": "#000000",
    },
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)