from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Length
from datetime import datetime

class ContactForm (FlaskForm):
    name = StringField('Name',
                        validators=[DataRequired(),
                        Length(min=2, max=30)],
                        render_kw={"placeholder":"Joe Jackson"})

    contact_info = StringField ('Phone Number Or Email',
                        validators=[DataRequired(),
                        Length(min=4, max=50)],
                        render_kw={"placeholder":"Your Phone Number or Email"})
      
    company_name = StringField ('Company Name',
                        validators=[Length(min=2, max=50)],
                        render_kw={"placeholder":"Your Company's Name (optional)"})

    help_description = TextAreaField ('How Can I Help?',
                        validators=[Length(min=2, max=300)],
                        render_kw={"placeholder":"Your Message (optional)"})

    # recaptcha = RecaptchaField()

    time_sent = StringField ('Time Sent',
                            default=datetime.now())

    submit = SubmitField('SUBMIT')
