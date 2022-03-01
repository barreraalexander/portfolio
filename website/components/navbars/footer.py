from flask import Markup, url_for


def component():
    return Markup(f"""
    <section id="footer_section">
        
        <div class="links_ctnr">

            <a href="https://github.com/barreraalexander" target="_blank">
                <div class="img_text_ctnr">
                    <img
                        src="{url_for('static', filename='images/assets/icons/github.svg')}"
                    >
                    <p>
                        github
                    </p>
                </div>
            </a>
            
            <a href="{url_for('static', filename='docs/BarreraAlexanderResume21.pdf')}" download>
                <div class="img_text_ctnr">
                    <img
                        src="{url_for('static', filename='images/assets/icons/resume.svg')}"
                    >
                    <p>
                        resume
                    </p>
                </div>
            </a>

            <a href="https://www.upwork.com/freelancers/~0120837e444852e684" target="_blank">
                <div class="img_text_ctnr">
                    <img
                        id="upwork"
                        src="{url_for('static', filename='images/assets/icons/upwork_logo.svg')}"
                    >
                    <p>
                        upwork
                    </p>
                </div>
            </a>

        </div>
        
        <div class="nav_ctnr">
            <h2>
                Navigation
            </h2>
            <ul>
                <a href="{url_for('main.index')}">
                    <li>
                        Home
                    </li>
                </a>

                <a href="{url_for('main.index')}">
                    <li>
                        Questions
                    </li>
                </a>

                <li>
                    Contact
                </li>
            </ul>
        </div>

    </section>
    """)