from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('_index.html')
