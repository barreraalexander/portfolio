from flask import Markup, url_for
from website.blueprints.main import unpack_elems

def component(variant):
    formatted_title = ""
    domain = ""
    domain_name = ""
    text_html_blob = ""
    role = ""
    github = ""
    logo_src = url_for('static', filename=f'images/assets/{variant}_logo.svg')

    if variant=="tod":
        formatted_title = "Technicians on Demand"
        domain = "https://www.technicianondemand.com/"
        domain_name = "technicianondemand.com"
        role = "Full Stack Dev"
        roles = {
            "role1": ('DESIGNER',
            "Designed the website in adobe xd.",
            "I also made changes to the design based on the requests of my client. Copies of the design were sent, and after approval I began building the site."
            ),
            "role2": ('CODER',
            "Built the website using html, sass, js and flask.",
            "The python flask framework is responsible for routing, as well as allowing me to produce components in the same way one would do for react. A simple clock was pulled from ThreeJS, and it's used to run the animatons."
            ),
            "role3": ('DEVOPS',
            "Launched the website on an ubuntu server, using nginx and gunicorn.",
            "I also garnered the ssl security certiface using site-bot. In order to save space on the server, I store a majority of the static files (images, videos) on AWS s3 buckets."
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
            "The backend dev built an api, and I was responsible for resolving requests, and building out certain ui components based on the data. One resolve included building out a report page with the data."
            ),
            "role2": ('CODER',
            "Built the frontend using html, css and  vanilla js.",
            "In order to make reusable components, I utilized python flasks Markup module. The components are React-like."
            ),
            "role3": ('SYSTEM CONTROLLER',
            "Worked with the team lead to manage git branches.",
            "This included everything from branching and merging, and resolving diffs."
            )
        }

    elif variant=="lit":
        formatted_title = "Goose Literature"
        domain = "http://18.119.119.99/"
        domain_name = "gooselit.com"
        github = ""
        role = "Full Stack Dev"
        github = """
            <a href="https://github.com/barreraalexander/gooselit">
                <p class="proj_link" data-variant={variant}>
                    Click here to see the github
                </p>
            </a>
        """
        roles = {
            "role1": ('DESIGNER',
            "I did not sit down and plan this project ui, as I normally would, I just worked off the cuff.",
            "To keep this style of build from getting difficult to manage, I made everything a component and gave them individual stylesheets (merged with SASS)."
            ),
            "role2": ('CODER',
            "I built the website using vanilla html, css, js, and python Flask.",
            "A special api was built to pull the content from a mysql database. The mysql database is running on AWS redis."
            ),
            "role3": ('DEVOPS',
            "I launched the website on an ubuntu server, using nginx and gunicorn.",
            "On this particular occassion, I wrote up a bash script that would setup the server to work with python flask. This turned a 2 hour task into a 15 minute one."
            )
        }

    elif variant=="port":
        formatted_title = "Barrera Portfolio"
        domain = "https://www.barrera-port.co/"
        domain_name = "www.barrera-port.co"
        role = "Full Stack Dev"
        github = """
            <a href="https://github.com/barreraalexander/portfolio">
                <p class="proj_link" data-variant={variant}>
                    Click here to see the github
                </p>
            </a>
        """
        roles = {
            "role1": ('DESIGNER',
            "I didn't build out the design, I just started coding.",
            "For this project, I wanted to use something."
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
            {github}
        </div>
    </div>
    
    """)

