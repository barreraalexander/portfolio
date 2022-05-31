from flask import Markup, url_for
from datetime import datetime
from website.components.pieces.button_like import component as button_like


def component():
    return Markup(f"""
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

    
    """)