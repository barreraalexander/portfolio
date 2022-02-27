from flask import Markup, url_for
from website.utils.webdata import CONTACT_DICT

from website.components.day_ctnr import component as day_ctnr

def component():
    resume_link = url_for('static', filename='docs/BarreraAlexanderResume21.pdf')
    mountain_link = "https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/mountain_cutout.png"


    moon_texture = url_for('static', filename='images/textures/moon_texture.png')
    normal_texture = url_for('static', filename='images/textures/normal_map.png')
    
    return Markup(f"""
    <section id="index_section1">
        <div class="hero_ctnr">
            <h1 id="hero_h1">
                WEB DEVELOPER
            </h1>
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
        <img id="mountain" src="{mountain_link}" alt="">

        <div id="night_ctnr"
            data-normal_texture="{normal_texture}"
            data-moon_texture="{moon_texture}"
        >
        </div>
        {day_ctnr()}
    </section>


    
    """)