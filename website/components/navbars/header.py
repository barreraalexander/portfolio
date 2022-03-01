from flask import Markup, url_for
from website.components.linkset import component as link_set

def component():
    return Markup(f"""
    <section id="header_section">
        <nav>
            <ul>

                <a href="{url_for('main.index')}">
                    <li class="brand">
                        Alexander Barrera
                    </li>
                </a>

                <a>
                    <img
                        id="hamburger"
                        src="{url_for('static', filename='images/assets/icons/hamburger.svg')}"
                        alt="menu toggle icon"
                        aria-label="menu"
                    >

                </a>

                <div class="main_links">
                    <a href="{url_for('main.index')}">
                        <li>
                            Home
                        </li>
                    </a>

                    <a href="{url_for('main.index')}">
                        <li>
                            Questions
                        </li>
                    </a>

                    <a href="{url_for('main.index')}">
                        <li>
                            Contact
                        </li>
                    </a>
                </div>

            </ul>
        </nav>
    </section>
    """)