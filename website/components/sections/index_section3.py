from flask import Markup
from website.components.tools_grid import component as tools_grid

def component():
    return Markup(f"""
    <section id="index_section3">
        <div class="dramatic_p_ctnr dramatic_p_ctnr_alt">
            <p>
                these are some
            </p>
            <p class='dramatic'>
                TOOLS
            </p>
            <p>
                I like to use
            </p>
        </div>
        {tools_grid()}
    </section>
    """)