from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.blueprints.api.forms import ContactForm

from website.components.project import component \
                                as project

from website.components.project_card import component \
                                as project_card
from website.components.day_ctnr import component \
                                as day_ctnr
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
def load_components ():
    return dict(META_DICT=META_DICT,
                CONTACT_DICT=CONTACT_DICT,
                project=project,
                project_card=project_card,
                technologies=technologies,
                day_ctnr=day_ctnr,
                about_me=about_me,
                work_flow=work_flow,
                q_a=q_a,
                comments=comments,
                link_set=link_set)

@main.route('/')
def index():
    return render_template('_index.html',
                            title='Home')


@main.route('/about')
def about():
    return render_template('_about.html',
                            title='About')

@main.route('/contact')
def contact():
    form = ContactForm()
    return render_template('_contact.html',
                            title='Contact',
                            form=form,
                            )

