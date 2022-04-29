from flask import Blueprint, render_template
# BASE
from website.utils.webdata import CONTACT_DICT, META_DICT
from website import cache

# SECTIONS
from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer
from website.components.navbars.hidden import component as hidden

from website.components.sections.contact_modal import component as contact_modal
from website.components.sections.comments import component as comments

from website.components.sections.hero import component as hero
from website.components.sections.story import component as story

main = Blueprint ('main', __name__)

@main.context_processor
def load_base ():
    return dict(
        header=header,
        footer=footer,
        contact_modal=contact_modal,
        hidden=hidden,
    )

@main.context_processor
def load_dicts ():
    return dict(
        META_DICT=META_DICT,
        CONTACT_DICT=CONTACT_DICT,
    )


@main.route('/')
@cache.cached(timeout=0)
def index():
    return render_template('_index.html',
        title='Home',
        hero=hero,
        story=story,
        comments=comments,
    )


@main.route('/about')
def about():
    return render_template('_about.html',
        title='About',
    )
