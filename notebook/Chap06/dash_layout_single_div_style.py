import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    # 各スタイルを設定
    style={
        "width": "500px",
        "height": "250px",
        "backgroundColor": "lime",
        "margin": "50px auto 50px",
    },
)

if __name__=="__main__":
    app.run_server(debug=True)