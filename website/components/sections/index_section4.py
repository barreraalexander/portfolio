from flask import Markup, url_for

from website.components.text_components import about_me \
                                as about_me
from website.components.text_components import work_flow \
                                as work_flow


def component():
    return Markup(f"""
    <section id="index_section4">
        <h2>
            ABOUT ME
        </h2>
        <div class="aboutme_ctnr">
            <img class="img_of_me"
                 src="https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/barrera.jpg"
                 alt="alexander barrera"
                 loading=lazy
            >
            <div class="aboutme_text_ctnr">
                <p class="aboutme_text">
                    name: alexander barrera 
                </p>
                <p class="aboutme_text">
                    job: web developer 
                </p>
                <p class="aboutme_text">
                    location: florida
                </p>
            </div>
        </div>
        {about_me()}
        {work_flow()}
    </section>
    """)