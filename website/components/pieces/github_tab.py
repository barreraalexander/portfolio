from flask import Markup, url_for
from website.utils.webdata import SOCIAL_MEDIA_LINKS

def component():
    return Markup(f"""
    <div class="github_tab">
        <img
            src="{ url_for('static', filename='images/assets/icons/github.svg') }"

        >
        <a href="{SOCIAL_MEDIA_LINKS.get('github')}/portfolio" target="_blank">
            <p>
                see the code for this website
            </p>
        </a>
    </div>
    """)