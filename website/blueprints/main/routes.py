from flask import Blueprint, render_template
# BASE
from website.utils.webdata import CONTACT_DICT, META_DICT
from website import cache

# SECTIONS
from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer
from website.components.navbars.hidden import component as hidden

from website.components.sections.contact_modal import component as contact_modal
from website.components.sections.resume_like import component as resume_like

from website.components.sections.hero import component as hero
from website.components.sections.story import component as story
from website.components.sections.about import component as about_section
from website.components.sections.skills import component as skills
from website.components.sections.styles import component as styles_section

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
@cache.cached(timeout=300)
def index():
    return render_template('_index.html',
        title='Home',
        hero=hero,
        story=story,
        resume_like=resume_like,
        skills=skills,
    )


@main.route('/about')
# @cache.cached(timeout=300)
def about():
    return render_template('_about.html',
        title='About',
        about_section=about_section,
    )

@main.route('/styles')
# @cache.cached(timeout=300)
def styles():
    return render_template('_styles.html',
        title='Styles',
        styles_section=styles_section,
    )
