from flask import Markup, url_for
from website.blueprints.main import unpack_elems

def component():
    # maybe this can be a sort of grid, moving animations?
    # talents = ["endurance", "api", "database management", "website build"]
    talents = {
        "tenacious" : {
            "description" : "Burning the night oil until the task is complete.",
            "theme_color" : "green",
        },
        "timely" : {
            "description" : "Never be late, and never be last.",
            "theme_color" : "blue"
        },
        "organized" : {
            "description" : "Organizing everyday keeps the headaches away.",
            "theme_color" : "red"
        },        
        "passionate" :  {
            "description" : "Clean, efficient code is such a beautiful thing.",
            "theme_color" : "purple"
        },
    }


    talent_divs = [f"""
    <div class="talent_card_ctnr" data-color="{talents[talent]['theme_color']}">
        <div class="talent_card_front">
            <p>
                {talent.upper()}
            </p>
            <img
                src="{url_for('static', filename=f'images/assets/{talent}.svg')}"
                alt="{talent}"
            >
        </div>
        <div class="talent_card_back">
            <p>
                {talents[talent]['description']}
            </p>
        </div>
    </div>    
    """ for talent in talents]

    return Markup(f"""
    <section id="talents_section">
        <div class="dramatic_p_ctnr dramatic_p_ctnr_alt">
            <p>
                These are the
            </p>
            <p class='dramatic'>
                TRAITS
            </p>
            <p>
                I possess
            </p>
        </div>
        <div class="talents_ctnr">
            {unpack_elems(talent_divs)}
        </div>

    </section>    
    
    """)