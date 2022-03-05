from flask import Markup, url_for
from website.utils.webdata import SOCIAL_MEDIA_LINKS

def component():
    return Markup(f"""
    <section id="footer_section">
        
        <div class="links_ctnr">

            <a href="{SOCIAL_MEDIA_LINKS.get('github')}" target="_blank">
                <div class="img_text_ctnr">
                    <img
                        src="{url_for('static', filename='images/assets/icons/github.svg')}"
                    >
                    <p>
                        github
                    </p>
                </div>
            </a>
            
            <a href="{url_for('static', filename='docs/BarreraAlexanderResume21.pdf')}" download>
                <div class="img_text_ctnr">
                    <img
                        src="{url_for('static', filename='images/assets/icons/resume.svg')}"
                    >
                    <p>
                        resume
                    </p>
                </div>
            </a>

            <a href="{SOCIAL_MEDIA_LINKS.get('upwork')}" target="_blank">
                <div class="img_text_ctnr">
                    <img
                        id="upwork"
                        src="{url_for('static', filename='images/assets/icons/upwork_logo.svg')}"
                    >
                    <p>
                        upwork
                    </p>
                </div>
            </a>

            <a href="{SOCIAL_MEDIA_LINKS.get('linkedin')}" target="_blank">
                <div class="img_text_ctnr">
                    <img
                        id="linkedin"
                        src="{url_for('static', filename='images/assets/icons/linkedin.svg')}"
                    >
                    <p>
                        linkedin
                    </p>
                </div>
            </a>

        </div>
        
        <div class="nav_ctnr">
            <h2>
                Navigation
            </h2>
            <ul>
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

                <li class="open_modal">
                    Contact
                </li>
            </ul>
        </div>

    </section>
    """)