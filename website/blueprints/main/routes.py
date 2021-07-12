from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.components.project_div import component as project_div
from website.components.linkset import component as link_set

from website.blueprints.main import CONTACT_DICT

main = Blueprint ('main', __name__)

@main.route('/')
def index():
    project_div1 = project_div(title="ppb", elem_id="project1")
    project_div2 = project_div(title="tod", elem_id="project2")
    project_div3 = project_div(title="browardreseller", elem_id="project3")
    return render_template('_index.html',
                            CONTACT_DICT=CONTACT_DICT,
                            project_div1=project_div1,
                            project_div2=project_div2,
                            project_div3=project_div3,
                            link_set=link_set)


@main.route('/about')
def about():
    return render_template('_about.html',
                            link_set=link_set,
                            CONTACT_DICT=CONTACT_DICT)

@main.route('/contact')
def contact():
    return render_template('_contact.html',
                            link_set=link_set,
                            CONTACT_DICT=CONTACT_DICT)

# @main.route('/new', methods=['GET', 'POST'])
# def index_new():
#     project_div1 = project_div(title="ppb", elem_id="project1")
#     project_div2 = project_div(title="tod", elem_id="project2")
#     project_div3 = project_div(title="browardreseller", elem_id="project3")
#     return render_template('_index_new.html',
#                             CONTACT_DICT=CONTACT_DICT,
#                             project_div1=project_div1,
#                             project_div2=project_div2,
#                             project_div3=project_div3)


# @main.route('/index2')
# def index2():
#     return render_template('_index2.html')