from fileinput import filename
from flask import Markup, url_for

def component(button_type, variant=""):

    all_dicts = {
        'contact' : {
            'href' : '',
            'inner_text' : 'Contact',
            'img_src' : url_for('static', filename='images/assets/icons/contact.svg'),
        },
        'call' : {
            'href' : '',
            'inner_text' : 'Call',
            'img_src' : url_for('static', filename='images/assets/icons/phone.svg'),
        },
        'resume' : {
            'href' : url_for('static', filename='docs/BarreraAlexanderResume21.pdf'),
            'href_config' : 'download', 
            'inner_text' : 'Resume',
            'img_src' : url_for('static', filename='images/assets/icons/resume.svg'),        }
    }

    button_dict = all_dicts.get(button_type)
    

    return Markup(f"""
    <a herf="{button_dict.get('href')}" {button_dict.get('href_config')}>
        <div class="button_like" data-variant="{variant}">
            <img
                src="{button_dict.get('img_src')}"
            >
            <p>
                {button_dict.get('inner_text')}
            </p>
        </div>
    </a>
     
    """)