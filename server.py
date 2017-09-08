from os import environ
import flask

app = flask.Flask(__name__)
app.run(environ.get('PORT'))
