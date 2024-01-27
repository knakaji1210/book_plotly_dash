import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Dashインスタンスを生成する
app = dash.Dash(__name__)

# コンポーネントをlayout属性に渡す
app.layout = dcc.Graph(
    # 引数figureにbar関数で作成したfigureを渡す
    figure = px.bar(x=[1,2,3,4,5], y=[1,2,3,4,5])
)

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)