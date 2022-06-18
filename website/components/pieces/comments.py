from flask import Markup

def component(title, elem_id=""):
    author_name = ""
    comment = ""
    origin = ""
    origin_url = ""



    if title=="ppb":
        author_name = "Russell Owens"
        comment = """I hired Alexander for a small HTML/CSS
        job. His code was well structured and the site looks
        good. He proactively identified issues and either
        fixed them or asked for guidance. He worked effectively
        with github branches, PRs and issue management. He was
        easy to work with and had a positive attitude."""
        origin = "www.privacyplaybook.com"
        origin_url = "https://privacyplaybook.com/"

    elif title=="tod":
        author_name = "Adrian Milian"
        comment = """He designed, created and launched my website.
                    Alexander was a huge help, super friendly and easy
                    to work with. I'll turn to him again if I need anything
                    for the web.
                """
        origin = "www.technicianondemand.com"
        origin_url = "https://www.technicianondemand.com/"

    elif title=="upwork1":
        author_name = "Jessica Baldwin"
        comment = """Alexander communicated exceptionally
        well and he worked on the task we provided
        expeditiously!""" 
        origin = "upwork"
        origin_url = "https://www.upwork.com/"


    elif title=="upwork2":
        author_name = "Port Vendre"
        comment = """Alexander was great to work with.
        Stayed on time, completed work exactly as asked,
        and provided quality coding. We would definitely
        recommend him and hope to work with him again!"""
        origin = "upwork"
        origin_url = "https://www.upwork.com/"

    elif title=="upwork3":
        author_name = "Preston Gordon"
        comment = """Alexander was great. He completed the
        job promptly and was a pleasure to work with. This
        job really helped me and my business. Thank you."""
        origin = "www.usindustrial.com"
        origin_url = "https://www.usindustrial.com/"


    return Markup(f"""
    <div class="comment_ctnr apply_shifting_border">
        <p class="comment">
            "{comment}"
        </p>
        <p class="author">
            -{author_name}
        </p>
        <a class="origin" href="{origin_url}" target="_blank">
            {origin}
        </a>
    </div>
    """)