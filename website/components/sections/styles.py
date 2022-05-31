from flask import Markup

from website.components.sections.neubrutalism import component as neubrutalism
from website.components.sections.minimalism import component as minimalism
from website.components.sections.glassmin import component as glassmin

def component():
    return Markup(f"""
    <section id="styles_section">
        {minimalism()}
        {glassmin()}
        {neubrutalism()}
    </section>
    """)