from flask import Markup, url_for

def component(set_type=""):
    dataset = ""
    if set_type=="main_nav":
        dataset = "data-mquery='hide_on_mobile'"
    
    home_link = url_for('main.index')
    about_link = url_for('main.about')
    contact_link = url_for('main.contact')
    return Markup (f"""
    <li {dataset}>
        <a href="{home_link}">
            Home
        </a>
    </li>
    <li {dataset}>
        <a href="{about_link}">
            Questions
        </a>
    </li>
    <li {dataset}>
        <a href="{contact_link}">
            Contact
        </a>
    </li>

    
    """)