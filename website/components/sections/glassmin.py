from flask import Markup, url_for
from website.components.pieces.button_like import component as button_like
from datetime import datetime

from website.components.pieces.glasspanel1 import component as gp1
from website.components.pieces.glasspanel2 import component as gp2
from website.components.pieces.glasspanel3 import component as gp3

def component():
    return Markup(f"""
    <section id="glassmin_section">
        <h1>
            Glass
        </h1>
        
        <div class="panels_ctnr">
            <div class="desktop_sidepanel">
                {gp1()}
                {gp2()}
            </div>
            {gp3()}
        </div>

    </section>
    <script src="{url_for('static', filename='js/animations/glassmin.js')}">
    </script>
    """)