import dash
from dash import html
from dash import dash_table
import pandas as pd

# 福岡県の避難所データを読み込む
df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")
print(df[:5])
print(df.columns)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            # dfの列名をリストにして引数columnsに渡す
            columns=[{"name": col, "id": col} for col in df.columns],
            # dfのデータを辞書型にして引数dataに渡す
            data=df.to_dict("records"),
        )
    ]
)

if __name__=="__main__":
    app.run_server(debug=True)