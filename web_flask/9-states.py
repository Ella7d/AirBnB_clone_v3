#!/usr/bin/python3
""" Starts a Flask web app and fetches data fromstorage engine """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(cls):
    """ Closes Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=None):
    """ Lists states from storage engine """
    if id:
        states = storage.all(State)
        key = 'State.' + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
