import dash
from dash_canvas import DashCanvas
from dash_canvas.utils import array_to_data_url
from skimage import io

# 画像を変数に渡す
data = array_to_data_url(io.imread("img/bird1.png"))
app = dash.Dash(__name__)

# レイアウトを作成する
app.layout = DashCanvas(
    id="first-image",
    image_content=data, # コンポーネントへの画像の読み込み
    width=800,
    lineWidth=12,
    goButtonTitle="nothing",
    lineColor="lime",
    hide_buttons=["zoom", "pan", "line", "select"],
)

if __name__=="__main__":
    app.run_server(debug=True)