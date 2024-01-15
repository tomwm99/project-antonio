# Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(children="Hello, Dash!"),  # Heading
        html.Div(
            children="""
            This is a basic Dash web application.
            """
        ),  # Text content
    ]
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)