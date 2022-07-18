from flask import Markup, url_for
from website.components.pieces.experience_card import component as experience_card
from website.components.pieces.dramatic_h1 import component as dramatic_h1

"""
so I want to highlight 3 pieces of experience,

technologies


in terms of design, I want each of the numbers to start on 0. 
scrolling to the section will make the number count up.

"""

def component():
    animation = url_for('static', filename='js/animations/experience.js')

    return Markup(f"""
    <section id="experience_section">
        {dramatic_h1('Lots of Experience')}
        <div class="experience_ctnr">
            {experience_card("successfully completed contracts", max_count=10)}
            {experience_card("technologies mastered", max_count=30)}
            {experience_card("successfully completed contracts", max_count=50)}
        </div>
        <div class="chart_ctnr">
            <canvas id="skills_chart"></canvas>
        </div>
    </section>
    <script src="{animation}">
    </script>
    
    """)