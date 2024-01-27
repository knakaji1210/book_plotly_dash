import dash  
# import dash_core_components as dcc
# これがdeprecatedということらしく
from dash import dcc
# これに置き換えた

# Dashインスタンスを生成する
app = dash.Dash(__name__)

app.layout = dcc.Dropdown()

if __name__=="__main__":
    # アプリケーションを起動する
    app.run_server(debug=True)