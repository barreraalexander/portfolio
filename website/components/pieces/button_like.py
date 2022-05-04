from fileinput import filename
from flask import Markup, url_for
from website.utils.webdata import CONTACT_DICT

def component(button_type, variant=""):

    all_dicts = {
        'contact' : {
            'href' : '',
            'inner_text' : 'Contact',
            'img_src' : url_for('static', filename='images/assets/icons/contact.svg'),
        },
        'call' : {
            'href' : f"tel:{CONTACT_DICT.get('phone')}",
            'inner_text' : 'Call',
            'img_src' : url_for('static', filename='images/assets/icons/phone.svg'),
            'variant' : 0,
        },
        'resume' : {
            'href' : url_for('static', filename='docs/BarreraAlexanderResume21.pdf'),
            'href_config' : 'download', 
            'inner_text' : 'Resume',
            'img_src' : url_for('static', filename='images/assets/icons/resume.svg'),
            'variant' : 1,
        }
    }

    button_dict = all_dicts.get(button_type)
    

    return Markup(f"""
    <a href="{button_dict.get('href')}" {button_dict.get('href_config')}>
        <div class="button_like" data-variant="{button_dict.get('variant')}">
            <img
                src="{button_dict.get('img_src')}"
            >
            <p>
                {button_dict.get('inner_text')}
            </p>
        </div>
    </a>
     
    """)