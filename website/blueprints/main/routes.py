from flask import Blueprint,\
    redirect, render_template,\
    request, url_for


# BASE
from website.utils.webdata import CONTACT_DICT, META_DICT

from website.components.contact_modal import component \
                                as contact_modal


# SECTIONS
from website.components.sections.hero import component \
                                as hero

# from website.components.sections.index_section2 import component \
#                                 as index_section2

# from website.components.sections.index_section3 import component \
#                                 as index_section3

# from website.components.sections.index_section4 import component \
#                                 as index_section4

# from website.components.sections.index_section5 import component \
#                                 as index_section5

# from website.components.sections.rain_scape import component \
#                                 as rain_scape

# from website.components.sections.passion_projects import component \
#                                 as passion_projects

# from website.components.sections.talents import component \
#                                 as talents

# from website.components.sections.upwork_section import component \
#                                 as upwork_section

from website.components.question_answer import component \
                                as q_a



from website.components.navbars.header import component as header
from website.components.navbars.footer import component as footer


main = Blueprint ('main', __name__)

@main.context_processor
def load_base ():
    return dict(
        header=header,
        footer=footer,
        contact_modal=contact_modal,
    )

@main.context_processor
def load_dicts ():
    return dict(
        META_DICT=META_DICT,
        CONTACT_DICT=CONTACT_DICT,
    )


@main.route('/')
def index():
    return render_template('_index.html',
        title='Home',
        hero=hero,
        # index_section1=index_section1,
        # index_section2=index_section2,
        # index_section3=index_section3,
        # index_section4=index_section4,
        # index_section5=index_section5,
        # upwork_section=upwork_section,
        # talents=talents,
        # passion_projects=passion_projects,
        # rain_scape=rain_scape,
    )


@main.route('/about')
def about():
    return render_template('_about.html',
        title='About',
        q_a=q_a,
    )
