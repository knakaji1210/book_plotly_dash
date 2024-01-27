import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# コンポーネントのスタイル設定
core_style = {"width": "80%", "margin": "5% auto"}

# Dashインスタンスを生成する
app = dash.Dash(__name__)

# レイアウトにdivの子要素として３つのコンポーネントを渡す
app.layout = html.Div(
    [ # 見出しを作成する
        html.H1("Hello Dash", style={"textAlign": "center"}),
        # ドロップダウンを作成する
        dcc.Dropdown(
            options=[
                {"label": "white", "value": "white"},
                {"label": "yellow", "value": "yellow"},
            ],
            value="white",
            style=core_style,
        ),
        # グラフを作成する
        dcc.Graph(
            figure = px.bar(x=[1,2,3,4,5], y=[1,2,3,4,5]),
            style=core_style,
        )
    ]
)


if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)