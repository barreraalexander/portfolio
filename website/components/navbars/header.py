from flask import Markup, url_for
from website.components.pieces.main_linkset import component as main_linkset
from website.components.pieces.button_like import component as button_like

def component():
    return Markup(f"""
    <section id="header_section">
        <nav>
            <ul>

                <a href="{url_for('main.index')}">
                    <li class="brand">
                        [ AB ]
                    </li>
                </a>

                <a>
                    <img
                        id="hamburger"
                        class="open_navigation_menu"
                        src="{url_for('static', filename='images/assets/icons/hamburger.svg')}"
                        alt="menu toggle icon"
                        aria-label="menu"
                    >
                </a>


                <div class="main_links">
                    {main_linkset()}
                </div>

                <div class="buttons_ctnr">
                    {button_like('call')}
                    {button_like('resume')}
                </div>

            </ul>
        </nav>
    </section>
    """)