import dash
from dash import dash_table

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    # 引数columnsに列名を渡す
    columns=[
        {"name": "number", "id": "number"},
        {"name": "region", "id": "area"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri"},
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
    # テーブル全体のセルのスタイルを定義
    style_cell={"width": 160, "fontSize": 24, "textAlign": "center"},
    # 列全体のスタイル
    style_cell_conditional=[
        # 条件は辞書で渡す
        {
            "if": {"column_id": "number"},
            # 条件を満たした場合の修飾
            "fontSize": 24,
            "backgroundColor": "#FFEEE4",
        }
    ],
    # ヘッダーのスタイル
    style_header_conditional=[
        {
            "if": {"column_id": "area"},
            "textAlign": "center",
            "width": 300,
        
        },
        {
            "if": {"column_id": "tsuyu-iri"},
            "backgroundColor": "#FBFFB9",
        }
    ],
    # データ部分のスタイル
    style_data_conditional=[
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "#FBFFB9",
        },
        # filter_queryを利用する場合、条件を""で囲って渡す
        {
            "if": {"column_id": "tsuyu-iri", "filter_query": "{number} > 3"},
            "backgroundColor": "#41D3BD",
        }
    ]
)

if __name__=="__main__":
    app.run_server(debug=True)