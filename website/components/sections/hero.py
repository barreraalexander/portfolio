from flask import Markup, url_for
from website.utils.webdata import CONTACT_DICT

def component():
    resume_link = url_for('static', filename='docs/BarreraAlexanderResume21.pdf')
    mountain_link = url_for('static', filename='images/assets/mountain_cutout.png')

    moon_model = url_for('static', filename='images/assets/three_d/moon.glb')
    ship_model = url_for('static', filename='images/assets/three_d/ship.glb')
    planet_model = url_for('static', filename='images/assets/three_d/planet.glb')

    animation_script = url_for('static', filename='js/animations/hero.js')
    three_d_script = url_for('static', filename='js/three_d/planets_mod.js')



    return Markup(f"""
    <section id="hero_section">
        <div class="hero_ctnr">
            <h2>
                OUT OF THIS WORLD
            </h2>
            <h1 id="hero_h1">
                WEB DEVELOPER
            </h1>
            <small>
                FROM SOUTH FLORIDA
            </small>
        </div>

        <img
            id="mountain"
            src="{mountain_link}"
            alt="mountain artifact"
        >

        <div
            id="night_ctnr"
            
            data-moon_model="{moon_model}"
            data-ship_model="{ship_model}"
            data-planet_model="{planet_model}"
        >
        </div>

    </section>

    <script
        src="{animation_script}">
    </script>

    <script
        src="{three_d_script}">
    </script>
    """)