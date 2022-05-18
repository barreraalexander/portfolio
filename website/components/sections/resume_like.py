from flask import Markup, url_for
from website.components.pieces.comments import component as comments
from website.components.pieces.dramatic_h1 import component as dramatic_h1

def component():
    observer = url_for('static', filename='js/animations/resume_like.js')

    return Markup(f"""
    <section id="resume_like">
        <img
            class="background_img"
            src="{url_for('static', filename='images/assets/icons/comment.svg')}"
            alt="resume like comment"

        >
        <div>
            {dramatic_h1('A Word from Past Clients')}
        </div>

        <div class="comments_ctnr">
            {comments('ppb')}
            {comments('tod')}
            {comments('upwork1')}
            {comments('upwork2')}
            {comments('upwork3')}
        </div>

    </section>
    <script
        src="{observer}">
    </script>
    """)