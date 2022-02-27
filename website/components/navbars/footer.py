from flask import Markup


def component():
    return Markup(f"""
    <section id="base_footer_section">
        <footer>
            <div class="footer_left">
                <h5>
                    Contact Me
                </h5>
                <ul>
                    <li>
                        <a href="tel:{{CONTACT_DICT['phone']}}">
                            ☎ {{CONTACT_DICT['phone']}}
                        </a>
                    </li>
                    <li>
                        <a href="#" class='open_modal'>
                            ✉ Fillout the Form
                        </a>
                    </li>
                </ul>
            </div>
            <div class="footer_right">
                <h5>
                    See my Works
                </h5>
                <ul>
                    <li>
                        <a href="{{CONTACT_DICT['github_link']}}">
                            Checkout my github 😺
                        </a>
                    </li>
                    <li>
                        <a href="{{url_for('static', filename='docs/BarreraAlexanderResume21.pdf')}}" download>
                            Download my resume 📃
                        </a>
                    </li>
                </ul>
            </div>
        </footer>
    </section>
    """)