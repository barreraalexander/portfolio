from flask import Markup, url_for
from website.components.pieces.button_like import component as button_like 
from website.components.pieces.dramatic_h1 import component as dramatic_h1


def component():
    script = url_for('static', filename='js/animations/story.js')

    return Markup(f"""
    <section id="story_section" loading="lazy">

        <img
            class="inksplat"
            src="{ url_for('static', filename='images/assets/ink2.svg') }"
        >
    
        <div class="text_ctnr">
            {dramatic_h1('Barrera')}
            <p>
                Alexander Barrera is a self-trained web developer from <span> south florida.</span>
            </p>
            <p>
                The framework he uses to build web apps and websites is <span> python flask.</span>
            </p>
            <p>
                He speaks in the third person. <span> Curious.</span>
                And he has a sense of humor when it comes to this whole <span> professionalism </span> thing.
            </p>
        </div>


        <img
            class="me_picture"
            src="{url_for('static', filename='images/assets/me1.png')}"
            alt="profile picture of alexander barrera"
            loading="lazy"
        >

        { button_like('call', variant=0) }
        { button_like('resume', variant=1) }

    </section>
    <script src="{script}">

    </script>
    
    """)