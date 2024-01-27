import plotly.graph_objects as go
from plotly.subplots import make_subplots

line_trace = go.Scatter(x=[0,1,2], y=[5,3,4], name="line")
scatter_trace = go.Scatter(
    x=[1,2,3], y=[2,1,5], mode="markers", name="scatter"
)
bar_trace = go.Bar(x=[1,2,3], y=[1,2,3], name="bar")
area_trace = go.Scatter(
    x=[3,4,5], 
    y=[5,3,4], 
    mode="none", 
    fillcolor="#1f77b4",
    fill="tozeroy",
    name="area",
)

subplots_fig = make_subplots(rows=2, cols=2)
subplots_fig.add_trace(line_trace, row=1, col=1)
subplots_fig.add_trace(scatter_trace, row=1, col=2)
subplots_fig.add_trace(bar_trace, row=2, col=1)
subplots_fig.add_trace(area_trace, row=2, col=2)

layout = go.Layout(width=600, height=600)
subplots_fig.update_layout(layout)
subplots_fig.show()