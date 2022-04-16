from flask import Markup, url_for
from website.components.pieces.main_linkset import component as main_linkset

def component():
    return Markup(f"""
    <section id="hidden_section">
        <div class="glass_back">
        </div>
        <div class="modal_ctnr">
            <nav>
                <ul>
                    {main_linkset()}
                </ul>
            </nav>
        </div>
    </section>
    """)