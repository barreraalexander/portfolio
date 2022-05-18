from flask import Markup, url_for
from website.utils.webdata import unpack_elems

def component(skill):
    skills = {
        'web_dev' : {
            'title' : 'Design to Build',
            'blurb' : 'If you want to provide the design, the differnce between design and product will be nill. I take pride in pixel perfect matching.',
            'img_src' : url_for('static', filename='images/assets/icons/skills/web_dev.svg'),
            'variant' : '1',
        },
        'db_management' : {
            'title' : 'Database Management',
            'blurb' : 'Certified db manager. Choose between mysql or postgres, generally hosted on AWS RDS.',
            'img_src' : url_for('static', filename='images/assets/icons/skills/db_management.svg'),
            'variant' : '2', 
        },
        'api_dev' : {
            'title' : 'API Development',
            'blurb' : 'Professional level API development, complete with correct status codes, and infiite scalabilty. The ORM can be pydantic, or graphql.',
            'img_src' : url_for('static', filename='images/assets/icons/skills/api_dev.svg'),
            'variant' : '1', 
        },
        'server' : {
            'title' : 'Elastic Cloud Server',
            'blurb' : 'Deployment on the server is so 2014. Take advantage of the seemless scalabaility of elastic servers that grow and shrink with your traffic.',
            'img_src' : url_for('static', filename='images/assets/icons/skills/server.svg'),
            'variant' : '2', 
        },
    }

    chosen_skill = skills[skill]

    dots = [
            """
            <div class="dot apply_shift_dot">
            </div>
            """
            for i in range(200)
        ]


    return Markup(f"""
    <div class="skill_card" data-variant="{chosen_skill.get('variant')}">
        <div class="dotted_bg_ctnr" data-variant="{chosen_skill.get('variant')}">
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