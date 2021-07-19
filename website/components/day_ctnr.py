from flask import Markup, url_for

def component():
    # img_src = url_for('static', filename='images/barrera_cutout.png')
    img_src = "https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/barrera_cutout.png"
    florida_svg = url_for('static', filename='images/assets/pink_florida.svg')
    resume_link = url_for('static', filename='docs/BarreraAlexanderResume21.pdf')
    contact_link = url_for('main.contact')
    return Markup(f"""
    <div id="day_ctnr">
        <div class="day_col left"> 
            <h3>
                WEB DEVELOPER.
            </h3>
            <div class="day_caption_ctnr">
                <p>
                    <span id="job_span">Coder</span> from south Florida
                </p>
                <img
                    src="{florida_svg}"
                >
            </div>
            <a href="{resume_link}" download>
                <button>
                    DOWNLOAD MY RESUME
                </button>
            </a>
            <a href="{contact_link}">
                <button>
                    CONTACT ME
                </button>
            </a>
        </div> 
        <div class="day_col right"> 
            <img
                src="{img_src}"
            >
        </div> 
    </div>
        
    """)