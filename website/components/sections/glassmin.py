from flask import Markup, url_for
from website.components.pieces.button_like import component as button_like
from datetime import datetime

def component():
    return Markup(f"""
    <section id="glassmin_section">
        <h1>
            Glass
        </h1>
        
        <div class="panels_ctnr">

            <div class="desktop_sidepanel">

                <div class="panel glass panel1">
                    <h2>
                        My Profile
                    </h2>
                    <div class="profile_ctnr">
                        <img
                            class="profile_img"
                            src="{ url_for('static', filename='images/assets/barrera_cutout.png') }"
                        >
                        <div class="profile_details">
                            <h3>
                                Alexander Barrera
                            </h3>
                            <small>
                                Hollywood, FL
                            </small>
                            <small>
                                {datetime.now().strftime("%I:%M %p")}
                            </small>
                            {button_like('available')}
                        </div>
                    </div>
                    <p>
                        Profile sections would look something like this. Often pushed off to the right and above non-essential information in desktop mode, and sitting at the top of the stack in mobile mode.
                    </p>
                </div>


                <div class="panel glass panel2">
                    <h2>
                        Nonessential Information
                    </h2>
                    <p>
                        Is pushed off to the right. This would often include the archive section of a news website or blog. On social media sites, the nonessential section would store advertisements, suggested friends and groups. 
                    </p>
                    <ul>
                        <li>
                            March 2022
                        </li>
                        <li>
                            February 2022
                        </li>
                        <li>
                            January 2022
                        </li>
                        <li>
                            December 2021
                        </li>
                        <li>
                            November 2021
                        </li>
                        <li>
                            October 2021
                        </li>
                        <li>
                            September 2021
                        </li>
                        <li>
                            August 2021
                        </li>
                        <li>
                            July 2021
                        </li>
                    </ul>
                </div>
            </div>

            <div class="panel glass panel3">
                <h2>
                    Structured Information
                </h2>
                <p>
                    Works beautifully with panels of glass. Everything is separated and sections are plainly labeled. Glass style is great for websites that have to display a lot of information.
                </p>
            </div>



        </div>

    </section>
    <script src="{url_for('static', filename='js/animations/glassmin.js')}">
    </script>
    """)