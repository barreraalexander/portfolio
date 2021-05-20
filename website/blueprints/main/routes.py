from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.components.project_div import component as project_div
from website.blueprints.main import CONTACT_DICT

main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    project_div1 = project_div(title="ppb", elem_id="project1")
    project_div2 = project_div(title="tod", elem_id="project2")
    project_div3 = project_div(title="browardreseller", elem_id="project3")
    return render_template('_index.html',
                            CONTACT_DICT=CONTACT_DICT,
                            project_div1=project_div1,
                            project_div2=project_div2,
                            project_div3=project_div3)
