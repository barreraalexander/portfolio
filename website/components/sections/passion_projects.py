from flask import Markup
from website.components.interactive_project_card import component as card

def component():
    return Markup(f"""
    <section id="passion_projects_section">
            <div class="dramatic_p_ctnr dramatic_p_ctnr_alt">
                <p>
                    some passion
                </p>
                <p class='dramatic'>
                    PROJECTS
                </p>
                <p>
                    I've developed
                </p>
            </div>
            <div class="interactive_project_cards_ctnr">
                {card(variant="lit")}
                {card(variant="port")}
            <div>
    </section>
    """)