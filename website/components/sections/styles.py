from flask import Markup

from website.components.sections.neubrutalism import component as neubrutalism
from website.components.sections.minimalism import component as minimalism
from website.components.sections.glassmin import component as glassmin
from website.components.sections.interactive_donut import component as interactive_donut
def component():
    return Markup(f"""
    <section id="styles_section">
        {interactive_donut()}
        {minimalism()}
        {glassmin()}
        {neubrutalism()}
    </section>
    """)