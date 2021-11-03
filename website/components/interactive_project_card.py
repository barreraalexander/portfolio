from flask import Markup, url_for
# data you'll need:

def component(variant):
    formatted_title = ""
    domain = ""
    domain_name = ""
    text_html_blob = ""
    role = ""
    logo_src = url_for('static', filename=f'images/assets/{variant}_logo.svg')

    if variant=="tod":
        formatted_title = "Technicians on Demand"
        domain = "https://www.technicianondemand.com/"
        domain_name = "www.technicianondemand.com"
        role = "Full Stack Dev"
        # logo_src = ""
        text_html_blob = """
        <ul class="text_blob">
            <li>
                Role 1
                <span class="expanded_text">
                    this is expanded text
                </span>
            </li>
        </ul>
        """

    elif variant=="ppb":
        formatted_title = "Privacy Playbook"
        domain = "https://privacyplaybook.com/"
        domain_name = "www.privacyplaybook.com"
        role = "Front End Dev"
        # logo_src = ""
        text_html_blob = """
        <ul class="text_blob">
            <li>
                Role 1
                <span class="expanded_text">
                    this is expanded text
                </span>
            </li>
        </ul>
        """

    elif variant=="lit":
        formatted_title = "Goose Literature"
        domain = "http://18.119.119.99/"
        domain_name = "www.gooselit.com"
        role = "Full Stack Dev"
        # logo_src = ""
        text_html_blob = """
        <ul class="text_blob">
            <li>
                Role 1
                <span class="expanded_text">
                    this is expanded text
                </span>
            </li>
        </ul>
        """

    return Markup(f"""
    <div class="interactive_project_card" data-variant={variant}>
        <div class="left_div">
            <h3>
                {role}
            </h3>
            {text_html_blob}
        </div>
        
        <div class="right_div">
            <h3>
                {formatted_title}
            </h3>
            <img
                id="{variant}_logo"
                src="{logo_src}"
                alt="{formatted_title} logo"
            >
        </div>
    </div>
    
    """)

