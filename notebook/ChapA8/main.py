from app import app
from layout import this_layout
import callback

app.layout = this_layout

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)