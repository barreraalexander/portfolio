from flask import Blueprint, request, flash, redirect, url_for
from website.utils.send_mail import send_form
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/send_mail', methods=['POST'])
def send_mail():
    form_data = []
    if request.method == 'POST':
        form_data = {
            'name' : request.form.get('name'),
            'contact_info' : request.form.get('contact_info'),
            'company_name' : request.form.get('company_name'),
            'time_sent' : datetime.now(),
            'help_description' : request.form.get('help_description'),
        }
        response = send_form(form_data)
        # response = 'FAIL'
        if response == 'SUCCESS':
            flash ('We got your message!')
            flash (f"We'll contact you at: {form_data['contact_info']}")
        elif response == 'FAIL':
            flash ("There's something wrong on our end. We're working on it now!")
        else:
            flash ("error")
        return redirect(url_for('main.index'))

    return redirect(url_for('main.index'))
