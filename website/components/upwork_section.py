from flask import Markup, url_for

def component():
    img_src = "https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/upwork_summary.png"
    upwork_logo = url_for('static', filename='images/assets/upwork_logo.svg')
    return Markup(f"""
    <section id="upwork_section">
        <h1>
            Upwork Profile
        </h1>
        <img
            class="upwork_logo"
            src="{upwork_logo}"
        >
        <div>
        </div>
        <img
            class="profile_summary"
            src="{img_src}"

        >
    </section>    
    
    """)
