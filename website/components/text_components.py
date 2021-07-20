from flask import Markup

def about_me():
    return Markup(f"""

        <p class="aboutme_paragraph">
            Hello! My name is
            <strong>
                Alexander Barrera
            </strong>
            and I'm a junior web developer from south Florida. When I'm not coding
            I like to go on
            <strong>
                long runs
            </strong>
                and
            <strong>
                read
            </strong> 
            fantasy novels (Lord of the Rings, anyone? 😊)
        </p>


    
    """)


def work_flow():
    return Markup(f"""

        <p class="workflow_text">
            These days, I like to use to use
            <strong>
                python flask
            </strong>
            when I'm building web apps. For the front end
            I'll usually utilize 
            <strong>
                SASS
            </strong>
            as well as
            <strong>
                GSAP
            </strong>
            and
            <strong>
                THREEJS
            </strong>
            libraries. For the database I like to use
            <strong>
                MySQL.
            </strong>
            For deployment, I like to use 
            <strong>
                ubuntu
            </strong>
            on
            <strong>
                nginx.
            </strong>
            Versional control with
            <strong>
                github.
            </strong>  
        </p>


    
    """)