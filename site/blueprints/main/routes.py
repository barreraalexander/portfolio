from flask import Blueprint,\
    redirect, render_template,\
    request, url_for
from portfolio import db

main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')