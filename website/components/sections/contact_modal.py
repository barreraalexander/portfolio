from flask import Markup, url_for
from website.blueprints.api.forms import ContactForm

def component():
    contact_form = ContactForm()
    send_mail_api = url_for('api.send_mail')
    return Markup(f"""
    <section id="contact_modal_section" data-status="closed">
        <div class="modal_ctnr">
            <p style="text-align:center;">
                Contact me form is disabled right now :)
            </p>
            <br>
            <p style="text-align:center;">
                Email: barreraalexander93@gmail.com
            </p>
            <form id="contact_form" action="{send_mail_api}" method="POST">
                {contact_form.hidden_tag()}
                <div class="form_ctnr">
                    <div id="cancel_ctnr">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#000000"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm5 13.59L15.59 17 12 13.41 8.41 17 7 15.59 10.59 12 7 8.41 8.41 7 12 10.59 15.59 7 17 8.41 13.41 12 17 15.59z"/></svg>
                    </div>
                    <div class="form_group">
                        {contact_form.name.label}
                        {contact_form.name}  
                    </div>
                    <div class="form_group">
                        {contact_form.contact_info.label}  
                        {contact_form.contact_info} 
                    </div>
                    <div class="form_group">
                        {contact_form.company_name.label}  
                        {contact_form.company_name}  
                    </div>
                    <div class="form_group">
                        {contact_form.help_description.label}  
                        {contact_form.help_description}
                    </div>
                    <div class="form_group">
                        {contact_form.recaptcha()}
                    </div>                    
                    <div class="form_group">
                        {contact_form.submit}  
                    </div>
                </div>
            </form>
        </div>
    </section>
    """)