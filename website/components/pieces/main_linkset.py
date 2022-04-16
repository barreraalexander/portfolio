from flask import Markup, url_for

def component():
    return Markup(f"""
    <a href="{url_for('main.index')}">
        <li>
            Home
        </li>
    </a>

    <a href="{url_for('main.about')}">
        <li>
            Questions 
        </li>
    </a>

    <li class="open_modal">
        Contact
    </li>
    """)