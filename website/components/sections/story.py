from flask import Markup, url_for

def component():
    script = url_for('static', filename='js/animations/story.js')

    return Markup(f"""
    <section id="story_section" loading="lazy">
        <img
            class="inksplat"
            src="{ url_for('static', filename='images/assets/ink2.svg') }"
        >
        <div class="text_ctnr">
            <h1>
                Barrera
            </h1>
            <hr>
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

        <a href="{url_for('static', filename='docs/BarreraAlexanderResume21.pdf')}" download>
            <button class="orange_btn">
                RESUME
            </button>
        </a>
        <button class="rev_orange_btn open_menu">
            CONTACT
        </button>
    </section>
    <script src="{script}">

    </script>
    
    """)