from flask import Markup, url_for

from website.components.interactive_project_card import component \
                                as interactive_project_card

def component():
    script_link = url_for('static', filename='js/components_js/interactive_project_card.js')

    return Markup(f"""
    <section id="index_section2">
        <div class="dramatic_p_ctnr">
            <p>
                These are some
            </p>
            <p class='dramatic'>
                CLIENTS
            </p>
            <p>
                I've worked with
            </p>
        </div>

        <div class="interactive_project_cards_ctnr">
            {interactive_project_card(variant="ppb")}
            {interactive_project_card(variant="tod")}
            <!-- {interactive_project_card(variant="us_ind")} -->
        </div>
        <script type="text/javascript" src="{script_link}"> </script>
    </section>
    
    """)