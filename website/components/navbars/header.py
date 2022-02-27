from flask import Markup, url_for
from website.components.linkset import component as link_set

def component():
    return Markup(f"""
    <section id="base_aside_section">
    <aside>
        <ul id="main_nav">
            <li class="h1_flexi">
                <a href="{url_for('main.index')}">
                    <h1>
                        Alexander Barrera
                    </h1>
                </a>
            </li>

            <li class="menu_flexi">
                <img
                    id="hamburger"
                    src="{url_for('static', filename='images/assets/hamburger.svg')}"
                    data-light_src="{url_for('static', filename='images/assets/hamburger_alt.svg')}"
                    data-dark_src="{url_for('static', filename='images/assets/hamburger.svg')}"
                    alt="nav button"
                >
            </li>
        </ul>
    </aside>
</section>
    """)