from flask import Markup, url_for
from website.components.pieces.main_linkset import component as main_linkset
from website.components.pieces.button_like import component as button_like

def component():
    return Markup(f"""
    <section id="hidden_section">
        <div class="glass_back">
        </div>
        <div class="modal_ctnr">
            <nav>
                <ul>
                    <img
                        id="close_hidden_menu"
                        class="close_navigation_menu"
                        src="{url_for('static', filename='images/assets/icons/cancel.svg')}"
                        alt="close icon"
                        aria-label="closes the mobile navigation menu"
                    >
                    {main_linkset()}
                    {button_like('call', variant=0)}
                    {button_like('resume', variant=1)}
                </ul>
            </nav>
        </div>
    </section>
    """)