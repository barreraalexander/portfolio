from flask import Markup, url_for
from website.blueprints.main import unpack_elems

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
        domain_name = "technicianondemand.com"
        role = "Full Stack Dev"
        roles = {
            "role1": ('DESIGNER',
            "Designed the website in adobe xd.",
            "this is the expanded text."
            ),
            "role2": ('CODER',
            "Built the website using html, sass, js and flask.",
            "this is the expanded text."
            ),
            "role3": ('DEVOPS',
            "Launched the website on an ubuntu server, using nginx and gunicorn.",
            "this is the expanded text."
            )
        }

    elif variant=="ppb":
        formatted_title = "Privacy Playbook"
        domain = "https://privacyplaybook.com/"
        domain_name = "privacyplaybook.com"
        role = "Front End Dev"
        roles = {
            "role1": ('COLLABORATOR',
            "Worked with the backend developer.",
            "to integrate data from an api into the frontend."
            ),
            "role2": ('CODER',
            "Built the front using html, css and  vanilla js.",
            "this is the expanded text."
            ),
            "role3": ('SYSTEM CONTROLLER',
            "Worked with the team lead to manage git branches.",
            "this is the expanded text."
            )
        }

    elif variant=="lit":
        formatted_title = "Goose Literature"
        domain = "http://18.119.119.99/"
        domain_name = "gooselit.com"
        role = "Full Stack Dev"
        roles = {
            "role1": ('DESIGNER',
            "I designed the website in adobe xd.",
            "this is the expanded text."
            ),
            "role2": ('CODER',
            "I built the website using vanilla html, css and js.",
            "this is the expanded text."
            ),
            "role3": ('DEVOPS',
            "I launched the website on an ubuntu server, using nginx and gunicorn.",
            "this is the expanded text."
            )
        }

    elif variant=="port":
        formatted_title = "Barrera Portfolio"
        domain = "https://www.barrera-port.co/"
        domain_name = "www.barrera-port.co"
        role = "Full Stack Dev"
        roles = {
            "role1": ('DESIGNER',
            "I designed the website in adobe xd.",
            "this is the expanded text."
            ),
            "role2": ('CODER',
            "I built the website using vanilla html, css and js.",
            "this is the expanded text."
            ),
            "role3": ('DEVOPS',
            "I launched the website on an ubuntu server, using nginx and gunicorn.",
            "this is the expanded text."
            )
        }


    work_lis = [
        f"""
        <li>
            <label>
                {roles[elem][0]}
            </label>
            <p>
            {roles[elem][1]}
            <span class="expanded_text">
                {roles[elem][2]}
            </span>
            </p>
        </li>
        """
        for elem in roles
    ]


    return Markup(f"""
    <div class="interactive_project_card" data-variant={variant}>
        <div class="left_div">
            <h3>
                {role}
            </h3>
            <ul class="text_blob" data-variant="{variant}">
                {unpack_elems(work_lis)}
            </ul>
        </div>
        
        <div class="right_div">
            <h3 data-variant="{variant}">
                {formatted_title}
            </h3>
            <img
                id="{variant}_logo"
                src="{logo_src}"
                alt="{formatted_title} logo"
            >
            <a href="{domain}">
                <p class="proj_link" data-variant={variant}>
                    {domain_name}
                </p>
            </a>
        </div>
    </div>
    
    """)

