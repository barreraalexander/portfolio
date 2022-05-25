from flask import Markup

from website.components.sections.neubrutalism import component as neubrutalism
from website.components.sections.minimalism import component as minimalism

def component():
    return Markup(f"""
    <section id="styles_section">
        {neubrutalism()}
        {minimalism()}
    </section>
    """)