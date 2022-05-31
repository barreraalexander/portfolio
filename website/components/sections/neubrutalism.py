from flask import Markup, url_for
from website.components.pieces.button_like import component as button_like


def component():
    return Markup(f"""
    <section id="neubrutalism_section">
        <div class="neu_hero_ctnr">
            <div class="neu_ctnr1">
                <div class="decorative_sqr">
                </div>
                <img
                    class="icon_bg"
                    src="{url_for('static', filename='images/assets/icons/bolt.svg')}"
                >
                <h1>
                    neu <br> <span>BRUTAL</span> <br> ism
                </h1>
                <div class="button_like_ctnr">
                    {button_like('call', variant='neu2')}
                    {button_like('resume', variant='neu1')}
                </div>

                <div class="circle_decoration_ctnr">
                    <div class="circle_dec circle1">
                    </div>
                    <div class="circle_dec circle2">
                    </div>
                </div>


            </div>
            <div class="neu_ctnr2">

                <div class="neu_card first_neu_card">
                    <p class="emoji_icon">
                        😁
                    </p>
                    <p>
                        More color is more fun! Tired of boring designs? Neubrutalism is meant to emphasize candy colors, inconsistent shapes, and heavy-usage of the built in canvas element.
                    </p>
                </div>

                <div class="neu_card second_neu_card">
                    <p class="emoji_icon_alt">
                        👍
                    </p>
                    <ul>
                        <li>
                            big time illustrions
                        </li>
                        <li>
                            lots of movement
                        </li>
                        <li>
                            sell fun products
                        </li>
                    </ul>
                </div>

                <div class="neu_card third_neu_card">
                    <p class="emoji_icon">
                        🐱‍👤
                    </p>
                    <p>
                        My inspiration was <a> gumroad.com </a>. Please check them out for an expert example of the neubrutalism design. But don't tell them I sent you <br> :)
                    </p>
                </div>


            </div>
        </div>

        <div class="neu_me_ctnr">

            <img
                class="barrera_cutout"
                src="{ url_for('static', filename='images/assets/barrera_cutout.png') }"
            
            >
            <p>
                This is me! In all my bald-headed glory!
            </p>
            <div class="circle_decoration circle_decoration1">
            </div>
            <div class="circle_decoration circle_decoration2">
            </div>

        </div>

        <div class="cta_ctnr">
            <div class="cta apply_shift_lr">
                <h3>
                    $
                </h3>
                <h2>
                    MEMORABLE WEB EXPERIENCE
                </h2>
                <h3>
                    $
                </h3>
                <h2>
                    TRY THIS BOLD STYLE
                </h2>
                <h3>
                    $
                </h3>
                <h2>
                    PERFECT FOR E-COMMERCE
                </h2>
                <h3>
                    $
                </h3>
                <h2>
                    MEMORABLE WEB EXPERIENCE
                </h2>
                <h3>
                    $
                </h3>
            </div>
        </div>
    </section>
    <script src="{url_for('static', filename='js/animations/neubrutalism.js')}">
    </script>
    """)