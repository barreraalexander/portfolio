from flask import Markup, url_for
from website.blueprints.api.forms import ContactForm

def component():
    contact_form = ContactForm()
    send_mail_api = url_for('api.send_mail')
    return Markup(f"""
    <section id="contact_modal_section" data-status="">
        <div class="glass_back">
        </div>
        <div class="modal_ctnr">
            <form
                id="contact_form"
                action="{send_mail_api}"
                method="POST"
            >
            
                {contact_form.hidden_tag()}
                <div class="form_ctnr">
                    <img
                        id="close_modal"
                        src="{url_for('static', filename='images/assets/icons/cancel.svg')}"
                    >

                    <div class="form_group">
                        <div class="label_ctnr">
                            {contact_form.contact_info.label}
                            <small>
                                | how I'll contact you 
                            </small> 
                        </div>
                        {contact_form.contact_info} 
                    </div>

                    <div class="form_group">
                        <div class="label_ctnr">
                            {contact_form.company_name.label}
                            <small>
                                | how I'll look you up :) 
                            </small> 
                        </div>
                        {contact_form.company_name}l  
                    </div>

                    <div class="form_group">
                        <div class="label_ctnr">
                            {contact_form.help_description.label}  
                            <small>
                                | I'm here to help
                            </small>
                        </div>
                        {contact_form.help_description}
                    </div>

                    <div class="form_group">
                        {contact_form.recaptcha()}
                    </div>                    
                    
                    <div class="form_group">
                        {contact_form.submit(class_="orange_btn")}  
                    </div>

                </div>
            </form>
        </div>
    </section>
    """)