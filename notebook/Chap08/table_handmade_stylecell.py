import dash
from dash import dash_table

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    # 引数columnsに列名を渡す
    columns=[
        {"name": "number", "id": "number", "clearable": True},
        {"name": "region", "id": "area", "deletable": True},
        {"name": "tsuyu-iri", "id": "tsuyu-iri", "editable": True},
    ],
    # 引数dataにデータを渡す
    data=[
        {"number": 0, "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    # テーブルを画面いっぱいに広げない
    fill_width=False,
    style_cell={"width": 160, "fontSize": 24, "textAlign": "center"},
)

if __name__=="__main__":
    app.run_server(debug=True)