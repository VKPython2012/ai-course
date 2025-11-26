import dash
from dash import html, dcc, Output, Input

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Simple Dash CallBack Demo"),

    dcc.Input(
        id="name-input",
        type="text",
        placeholder="Type your name...",
        style={"marginRight": "10px"}
    ),

    html.Div(id="output-text", style={"marginTop": "20px"})
])

# Decorator
@app.callback(
    Output("output-text", "children"),
    Input("name-input", "value")
)
def update_output(value):
    if not value:
        return "Waiting for input..."
    else:
        return f"Hello {value}!"

if __name__ == "__main__":
    app.run(debug=True)