import dash
from dash import dcc
from dash import html

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)
app.config.suppress_callback_exceptions = True

tab_selected_style = {
    "backgroundColor": "limegreen",
    "color": "white",
    "fontWeight": "bold",
}

app.layout = html.Div(
    [
        # Uploadコンポーネントを配置する
        dcc.Upload(
            id="uploadp-csv",
            children=html.Div(
                ["Drag and Drop or ", html.A("Select CSV or Excel File")]  # <a>タグ（anchor）
            ),
            style={
                "width": "80%",
                "height": "100px",
                "lineHeight": "60%",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "30px",
                "textAlign": "center",
                "margin": "5% auto",
            },
        ),
        # テーブルとグラフの表示を切り替えるタブ
        dcc.Tabs(
            id="tabs",
            value="one",
            children=[
                # テーブルを表示するタブ
                dcc.Tab(
                    label="Table",
                    value="one",
                    selected_style=tab_selected_style,
                    children=[html.Div(id="upload-content")],
                ),
                # ドロップダウンとグラフを表示するタブ
                dcc.Tab(
                    label="Graph1",
                    value="two",
                    selected_style=tab_selected_style,
                    children=[
                        html.Div(
                            [
                                dcc.Dropdown(id="table-dropdown", multi=True),
                                html.Div(id="update_graph1")
                            ]
                        )
                    ],                      
                ),
                dcc.Tab(
                    label="Graph2",
                    value="three",
                    selected_style=tab_selected_style,
                    children=[
                        html.Div(
                            [
                                html.Div(id="update_graph2")
                            ]
                        )
                    ],                      
                ),                
            ],
        ),
    ]
)


if __name__=="__main__":
    app.run_server(debug=True)