from flask import Markup, url_for

def component():
    img_src = "https://barrera-portfolio-static.s3.us-east-2.amazonaws.com/barrera_cutout.png"
    florida_svg = url_for('static', filename='images/assets/theme_florida.svg')
    resume_link = url_for('static', filename='docs/BarreraAlexanderResume21.pdf')
    return Markup(f"""
    <div id="day_ctnr">
        <div class="day_col left"> 
            <h3>
                WEB DEVELOPER
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
                    Download My Resume
                </button>
            </a>
            <a href="#" class="open_modal">
                <button>
                    Contact Me
                </button>
            </a>
            <div class="color_picker">
                <p>
                    pick an accent
                </p>
                <div class="color_div" data-bg_color="#EDFFE1"></div>
                <div class="color_div" data-bg_color="#E1FFF9"></div>
                <div class="color_div" data-bg_color="#FCE1FF"></div>
                <div class="color_div" data-bg_color="#FAFFE1"></div>
            </div>
        </div>
        <div class="day_col right"> 
            <img
                src="{img_src}"
            >
        </div> 
    </div>
        
    """)