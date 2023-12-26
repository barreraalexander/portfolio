from flask import Blueprint, render_template


# SECTIONS
from website.utils.webdata import CONTACT_DICT, META_DICT
from website.components.sections.contact_modal import component as contact_modal
from website import schemas

from website.templates.components.forms.forms import ContactForm

main = Blueprint ('main', __name__)

@main.context_processor
def load_base ():
    return dict(
        # footer=footer,
        # contact_modal=contact_modal,
        contact_form=ContactForm()
        # github_tab=github_tab,
        # socials_schema=schemas.socialMediaLinks()
    )

@main.context_processor
def load_dicts ():
    return dict(
        META_DICT=META_DICT,
        CONTACT_DICT=CONTACT_DICT,
        contact_schema=schemas.contactLanguage(),
        meta_schema=schemas.metaLanguage(),
        socials_schema=schemas.socialMediaLinks(),
        comment_schemas=schemas.comments()
    )


@main.route('/')
def index():
    return render_template('index.html',
        title='Home',
        # home_section=home_section,
        skill_schemas=schemas.skills(),
        experience_schemas=schemas.experiences()
    )


@main.route('/styles')
def styles():
    return render_template('styles.html',
        title='Styles',
        # styles_section=styles_section
    )
