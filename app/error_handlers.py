import flask
from app import app


@app.errorhandler(404)
def error_404(error):
    return flask.render_template('404_error.html'), 404
