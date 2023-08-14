from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    # return 'This is main blueprint'
    return render_template('index.html')

