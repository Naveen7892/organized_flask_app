from app.questions import bp
from flask import render_template

@bp.route('/')
def index():
    return render_template('questions/index.html')