import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# データの読み込み
iris = px.data.iris()

print("iris.columns = ", iris.columns)

options = [{"label": col, "value": col} for col in iris.columns[:4]]
print("options = ", options)

iris_df = iris[["sepal_length", "sepal_width"]]
print("iris_df = ", iris_df)

print('iris_df["sepal_length"]= ', iris_df["sepal_length"])

cells = [iris_df[col].tolist() for col in iris_df.columns]
print(cells)
