from flask import redirect, url_for, render_template, flash

from frontend_tutorial import app, db


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
