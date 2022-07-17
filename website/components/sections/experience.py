from flask import Markup, url_for
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
            <div class="experience" data-max_count="10">
                <h3>
                    0
                </h3>
                <p>
                    successfully completed contracts
                </p>
            </div>
            <div class="experience" data-max_count="30">
                <h3>
                    0
                </h3>
                <p>
                    technologies mastered
                </p>
            </div>
            <div class="experience" data-max_count="50">
                <h3>
                    0
                </h3>
                <p>
                    successfully completed contracts
                </p>
            </div>

        </div>
    </section>
    <script src="{animation}">
    </script>
    
    """)