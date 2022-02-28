from flask import Markup, url_for
from website.utils.webdata import CONTACT_DICT

def component():
    resume_link = url_for('static', filename='docs/BarreraAlexanderResume21.pdf')
    mountain_link = url_for('static', filename='images/assets/mountain_cutout.png')

    moon_texture = url_for('static', filename='images/textures/moon_texture.png')
    normal_texture = url_for('static', filename='images/textures/normal_map.png')
    
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
            
            <div class="caption_ctnr">
                <p>
                    Full Stack Web Developer from south Florida
                </p>
                <a href="{CONTACT_DICT['github_link']}">
                    Checkout my github 😺
                </a>
                <a href="{resume_link}" download>
                    <button>
                        Download my Resume 📃         
                    </button>
                </a>
            </div>
        </div>

        <img
            id="mountain"
            src="{mountain_link}"
            alt="mountain artifact"
        >

        <div
            id="night_ctnr"
            data-normal_texture="{normal_texture}"
            data-moon_texture="{moon_texture}"
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