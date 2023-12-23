from flask import Markup

from website.components.sections.story import component as story
from website.components.sections.skills import component as skills
from website.components.sections.experience import component as experience
from website.components.sections.resume_like import component as resume_like

def component():
    return Markup(f"""
    <section id="index_section">

    </section>
    
    
    
    """)


        # {hero()}
        # {skills()}
        # {experience()}
        # {story()}
        # {resume_like()}