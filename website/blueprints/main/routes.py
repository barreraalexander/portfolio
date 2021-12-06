from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.components.passion_projects import component \
                                as passion_projects

from website.components.talents import component \
                                as talents
from website.components.tools_grid import component \
                                as tools_grid
from website.components.project_card import component \
                                as project_card
from website.components.interactive_project_card import component \
                                as interactive_project_card
from website.components.upwork_section import component \
                                as upwork_section
from website.components.day_ctnr import component \
                                as day_ctnr
from website.components.contact_modal import component \
                                as contact_modal
from website.components.technologies import component \
                                as technologies
from website.components.linkset import component \
                                as link_set
from website.components.comments import component \
                                as comments
from website.components.text_components import about_me \
                                as about_me
from website.components.text_components import work_flow \
                                as work_flow
from website.components.question_answer import component \
                                as q_a
from website.blueprints.main import CONTACT_DICT, META_DICT

main = Blueprint ('main', __name__)

@main.context_processor
def load_dicts ():
    return dict(META_DICT=META_DICT,
                CONTACT_DICT=CONTACT_DICT)


@main.context_processor
def load_components ():
    return dict(project_card=project_card,
                interactive_project_card=interactive_project_card,
                technologies=technologies,
                day_ctnr=day_ctnr,
                about_me=about_me,
                work_flow=work_flow,
                q_a=q_a,
                comments=comments,
                contact_modal=contact_modal,
                upwork_section=upwork_section,
                tools_grid=tools_grid,
                talents=talents,
                passion_projects=passion_projects,
                link_set=link_set)

@main.route('/')
def index():
    return render_template('_index.html',
                            title='Home')


@main.route('/about')
def about():
    return render_template('_about.html',
                            title='About')
