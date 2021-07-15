import secrets
from flask_mail import Message
from website import mail
from datetime import datetime
from secrets import token_hex

MAIN_RECIPIENT = "barreraalexander93@gmail.com"

def send_form (form_data):
    
    msg = Message(f'PORTFOLIO CONTACT REQUEST | MESSAGE_ID:{token_hex(6)}',
                recipients=[MAIN_RECIPIENT])
    msg.body = (f"""

    NAME: {form_data['name']}
    
    CONTACT INFO: {form_data['contact_info']}
        
    COMPANY NAME: {form_data['company_name']}
        
    TIME SENT : {form_data['time_sent'].strftime('%B %d, %Y    %I:%M %p')}
    \n
    MESSAGE
    -------
    {form_data['help_description']}
    """)

    try:
        mail.send(msg)
        return 'SUCCESS'
    except Exception as err:
        error_explanation = (f""" Yikes, our email system is down """)
        print (error_explanation)
        print (err)
        return 'FAIL' 
