import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # スライダの作成
        dcc.Slider(
            id="myslider",
            min=-10,
            max=100,
            step=1,
            value=50,
            marks={
                -10: {
                    "label": "-10度",
                    "style": {"color": "blue", "fontSize": 30},
                },
                0: {"label": "0", "style": {"fontSize": 40}},
                25: "25度",
                50: {"label": "50度", "style": {"fontSize": 50}},
                75: "75度",
                100: {
                    "label": "100度",
                    "style": {"color": "red", "fontSize": 40},
                },
            },
            dots=True,
        )
    ],
    style={"width": "80%","margin": "3% auto"},
)

if __name__=="__main__":
    app.run_server(debug=True)