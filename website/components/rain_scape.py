from flask import Markup, url_for

def component():
    smoke_texture = url_for('static', filename='images/textures/smoke.png')
    js = url_for('static', filename='js/index_js/rain_scape.js')
    return Markup(f"""
    <section id="rain_scape_section">
        <h1>
            FRONTEND DEV
        </h1>
        <h1>
            DB MANAGER
        </h1>
        <h1>
            CODER CODER
        </h1>
        <div id="rain_scape_ctnr" data-smoke_texture="{smoke_texture}">
        </div>
    </section>
    """)