from flask import Markup, url_for
from website.utils.webdata import unpack_elems

def component(skill):
    skills = {
        'web_dev' : {
            'title' : 'Design to Build',
            'blurb' : 'Pixel perfect matching between design and build',
            'img_src' : url_for('static', filename='images/assets/icons/skills/web_dev.svg'),
        },
        'db_management' : {
            'title' : 'Database Management',
            'blurb' : 'Certified db manager, choose between ',
            'img_src' : url_for('static', filename='images/assets/icons/skills/db_management.svg'),
        },
        'api_dev' : {
            'title' : 'API Development',
            'blurb' : 'Professional level ',
            'img_src' : url_for('static', filename='images/assets/icons/skills/api_dev.svg'),
        },
        'server' : {
            'title' : 'Elastic Cloud Server',
            'blurb' : 'Deployment on the server is so 2014. Take advantage of the seemless scalabaility of elastic servers that grow and shrink with your traffic.',
            'img_src' : url_for('static', filename='images/assets/icons/skills/server.svg'),
        },
    }

    chosen_skill = skills[skill]

    dots = [
            """
            <div class="dot">
            </div>
    
    
            """
            for i in range(300)
        ]


    return Markup(f"""
    <div class="skill_card">
        <div class="dotted_bg_ctnr">
            {unpack_elems(dots)}
        </div>
        <div class="skill_card_contents">
            <img
                class="skill_img"
                src="{chosen_skill.get('img_src')}"
                alt=""

            >
            <h2>
                {chosen_skill.get('title')}
            </h2>
            <p>
                {chosen_skill.get('blurb')}
            </p>
        </div>
    </div>    
    """)