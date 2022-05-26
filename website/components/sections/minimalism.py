from flask import Markup
from website.components.pieces.button_like import component as button_like

def component():
    return Markup(f"""
    <section id="minimalism_section">
        <div class="hero_text_ctnr">
            <h1>
                Minimal
            </h1>
            <p class="description">
                The go-to style for IT companies, 
            </p>
            <div class="buttons_ctnr">
                {button_like('call')}
                {button_like('resume')}
            </div>
        </div>
    </section>
    """)