from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request
from flask import url_for, redirect

moje_imie = "Nela TheMaster"
msg = "Witaj swiecie!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)


@app.route('/ui')
def ui():
    return redirect(url_for('static', filename='index.html'))
