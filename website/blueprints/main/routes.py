from flask import Blueprint, render_template


# SECTIONS
from website.utils.webdata import CONTACT_DICT, META_DICT

# BASE
# from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer
# from website.components.navbars.hidden import component as hidden
from website.components.pieces.github_tab import component as github_tab
from website.components.sections.contact_modal import component as contact_modal

# PAGES
from website.components.pages.styles import component as styles_section
from website.components.pages.home import component as home_section

from website import schemas

main = Blueprint ('main', __name__)

@main.context_processor
def load_base ():
    return dict(
        footer=footer,
        contact_modal=contact_modal,
        github_tab=github_tab,
        # socials_schema=schemas.socialMediaLinks()
    )

@main.context_processor
def load_dicts ():
    return dict(
        META_DICT=META_DICT,
        CONTACT_DICT=CONTACT_DICT,
        contact_schema=schemas.contactLanguage(),
        meta_schema=schemas.metaLanguage(),
        socials_schema=schemas.socialMediaLinks()
    )


@main.route('/')
def index():
    return render_template('index.html',
        title='Home',
        home_section=home_section,
        skill_schemas=schemas.skills(),
        experience_schemas=schemas.experiences()
    )


@main.route('/styles')
def styles():
    return render_template('styles.html',
        title='Styles',
        styles_section=styles_section
    )
