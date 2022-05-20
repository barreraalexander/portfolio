from flask import Markup

from website.components.sections.neubrutalism import component as neubrutalism
from website.components.sections.minimalism import component as minimalism

def component():
    return Markup(f"""
    <section class="styles_section">
        {neubrutalism()}
        {minimalism()}
    </section>
    """)