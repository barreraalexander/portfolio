from flask import Blueprint, render_template

# SECTIONS
from website import schemas

from website.templates.components.forms.forms import ContactForm

main = Blueprint ('main', __name__)

@main.context_processor
def load_base ():
    return dict(
        contact_form=ContactForm()
    )

@main.context_processor
def load_dicts ():
    return dict(
        contact_schema=schemas.contactLanguage(),
        meta_schema=schemas.metaLanguage(),
        socials_schema=schemas.socialMediaLinks(),
    )


@main.route('/')
def index():
    return render_template('index.html',
        title='Home',
        # home_section=home_section,
        skill_schemas=schemas.skills(),
        experience_schemas=schemas.experiences(),
        comment_schemas=schemas.comments()

    )


@main.route('/styles')
def styles():
    return render_template('styles.html',
        title='Styles',
        # styles_section=styles_section
    )
