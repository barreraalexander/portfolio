from flask import Markup, url_for

from website.components.comments import component \
                                as comments


def component():
    return Markup(f"""
    <section id="index_section5">
        <div class="dramatic_p_ctnr">
            <p>
                a few
            </p>
            <p class='dramatic'>
                WORDS
            </p>
            <p>
                from past clients
            </p>
        </div>
        <div class="comments_ctnr">
            <div class="comment_svg_ctnr">
                <svg id="comment_svg"
                    xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#000000"><path d="M0 0h24v24H0z" fill="none"/><path d="M21.99 4c0-1.1-.89-2-1.99-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4-.01-18zM18 14H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/>
                </svg>
            </div>
            {comments("ppb")}
            {comments("upwork1")}
            {comments("upwork2")}
            {comments("upwork3")}
            {comments("tod")}
        </div>
    </section>    
    """)