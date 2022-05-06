from flask import Markup
from website.components.pieces.comments import component as comments

def component():
    return Markup(f"""
    <section id="resume_like">
        <div>
            <h1>
                A Word from Past Clients
            </h1>

        </div>
        <div class="comments_ctnr">
            {comments('ppb')}
            {comments('tod')}
            {comments('upwork1')}
            {comments('upwork2')}
            {comments('upwork3')}
        </div>
    </section>
    """)