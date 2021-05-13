from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.components.project_div import component as project_div

main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    project_div1 = project_div(title="food")
    project_div2 = project_div(title="tod")
    
    return render_template('_index.html',
                            project_div1=project_div1,
                            project_div2=project_div2)
