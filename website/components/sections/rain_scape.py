from flask import Markup, url_for

def component():
    smoke_texture = url_for('static', filename='images/textures/smoke.png')
    js = url_for('static', filename='js/index_js/rain_scape.js')
    return Markup(f"""
    <section id="rain_scape_section">
        <div class="cards_ctnr">
            <div class="card">
                <p>
                    RESPONSIVE 3D INTERFACES
                </p>
            </div>
            <div class="card">
                <p>
                    MANAGED DATABASES
                </p>
            </div>
            <div class="card">
                <p>
                    PYTHON FRAMEWORKS
                </p>
            </div>    
        </div>
        <div id="rain_scape_ctnr" data-smoke_texture="{smoke_texture}">
        </div>
    </section>
    """)