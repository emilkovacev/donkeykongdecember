from flask import Flask
from flask import render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def december():
    return render_template('dk.html', is_december=datetime.now().month == 12)

@app.route('/static/<file>')
def serve_static(file):
    return send_from_directory('static', file)

