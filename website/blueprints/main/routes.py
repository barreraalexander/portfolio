from flask import Blueprint,\
    redirect, render_template,\
    request, url_for

from website.blueprints.api.forms import ContactForm

from website.components.project import component \
                                as project
from website.components.technologies import component \
                                as technologies
from website.components.linkset import component \
                                as link_set

from website.blueprints.main import CONTACT_DICT

main = Blueprint ('main', __name__)

@main.route('/')
def index():
    return render_template('_index.html',
                            CONTACT_DICT=CONTACT_DICT,
                            project=project,
                            technologies=technologies,
                            link_set=link_set)


@main.route('/about')
def about():
    return render_template('_about.html',
                            link_set=link_set,
                            CONTACT_DICT=CONTACT_DICT)

@main.route('/contact')
def contact():
    form = ContactForm()
    return render_template('_contact.html',
                            form=form,
                            link_set=link_set,
                            CONTACT_DICT=CONTACT_DICT)

