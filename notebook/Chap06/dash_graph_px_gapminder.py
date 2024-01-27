import dash
from dash import dcc
import plotly.express as px

gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

app = dash.Dash(__name__)

app.layout = dcc.Graph(
    # 引数figureにPlotly Expressで作成したfigureを直接渡す
    figure = px.scatter(
        gapminder2007,
        x="gdpPercap",
        y="pop",
        size="lifeExp",
        color="continent",
        hover_name="country",
        log_x=True,
        log_y=True,
        title="Gapminder",
    )
)

if __name__=="__main__":
    app.run_server(debug=True)