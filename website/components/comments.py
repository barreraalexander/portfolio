from flask import Markup

def component(title, elem_id=""):
    author_name = ""
    comment = ""
    if title=="ppb":
        author_name = "Russell Owens"
        comment = "I hired Alexander for a small HTML/CSS job. His code was well structured and the site looks good. He proactively identified issues and either fixed them or asked for guidance. He worked effectively with github branches, PRs and issue management. He was easy to work with and had a positive attitude."

    elif title=="tod":
        author_name = "Adrian Milian"
        comment = "This is the comment commment" 

    elif title=="upwork1":
        author_name = "Jessica Baldwin"
        comment = "Alexander communicated exceptionally well and he worked on the task we provided expeditiously!" 

    elif title=="upwork2":
        author_name = "Port Vendre"
        comment = "Alexander was great to work with. Stayed on time, completed work exactly as asked, and provided quality coding. We would definitely recommend him and hope to work with him again!" 


    return Markup(f"""
    <div class="comment_ctnr">
        <p class="comment">
            "{comment}"
        </p>
        <p class="author">
            -{author_name}
        </p>
    </div>
    """)