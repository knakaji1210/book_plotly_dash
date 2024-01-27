import dash  
import dash_html_components as html  

# Dashインスタンスを生成する
app = dash.Dash(__name__)

# コンポーネントをlayout属性に渡す
app.layout = html.H1(
    "Hello Dash",
    # スタイルを設定する
    style={"color": "red", "textAlign": "center"},
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)