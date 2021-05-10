import dash
import dash_auth
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SUPERHERO])

auth = dash_auth.BasicAuth(
    app,
    {'hello3': 'world3'}
)


# app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
#application = app.server