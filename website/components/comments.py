from flask import Markup

def component(title, elem_id=""):
    author_name = ""
    comment = ""
    if title=="ppb":
        author_name = "Russell Owens"
        comment = "This is the comment commment" 

    if title=="tod":
        author_name = "Adrian Milian"
        comment = "This is the comment commment" 




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