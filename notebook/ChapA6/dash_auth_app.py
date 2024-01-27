import dash
import dash_auth
from dash import html

pass_pair = {"plotly": "dash", "test": "test1"}

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

auth = dash_auth.BasicAuth(app, pass_pair)

app.layout = html.H1("Plotly Dash Bookへようこそ！", style={"textAlign": "center"})

if __name__ == "__main__":
    app.run_server(debug=True)