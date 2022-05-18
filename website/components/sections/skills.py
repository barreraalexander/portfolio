from flask import Markup, url_for
from website.components.pieces.dramatic_h1 import component as dramatic_h1
from website.components.pieces.skill_card import component as skill_card

def component():
# slide in each card


    return Markup(f"""
    <section id="skills_ctnr">
        {dramatic_h1('Type of Work I Do')}
        <div class="skill_cards_ctnr">
            {skill_card('web_dev')}
            {skill_card('db_management')}
            {skill_card('api_dev')}
            {skill_card('server')}
        </div>
    </section>
    <script src="{url_for('static', filename='js/animations/skill_card.js')}">
    </script>
    """)