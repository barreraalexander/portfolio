from flask import Blueprint,\
    redirect, render_template,\
    request, url_for
from website import db

main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('_index.html')

@main.route('/oldindex', methods=['GET', 'POST'])
def oldindex():
    return render_template('_oldindex.html')