from flask import Markup, url_for
from website.components.pieces.comments import component as comments

def component():
    observer = url_for('static', filename='js/animations/resume_like.js')

    return Markup(f"""
    <section id="resume_like">
        <div>
            <h1>
                A Word from Past Clients
            </h1>
            <hr>
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