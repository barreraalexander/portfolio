from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from datetime import datetime

class ContactForm (FlaskForm):
    contact_info = StringField('Email',
                        validators=[
                            DataRequired(),
                            Length(min=4, max=50),
                            Email(),
                        ],
                        render_kw={
                            "placeholder":"Email",
                        }
                    )
      
    company_name = StringField ('Company',
                        validators=[
                            Length(min=2, max=50),
                        ],
                        render_kw={
                            "placeholder":"Your Company's Name (optional)",
                        }
                    )

    help_description = TextAreaField ("What's Up?",
                        validators=[
                            DataRequired(),
                            Length(min=2, max=300),
                        ],
                        render_kw={
                            "placeholder":"Your Messages"
                        }
                    )

    recaptcha = RecaptchaField()

    time_sent = StringField ('Time Sent',
                            default=datetime.now())

    submit = SubmitField('SUBMIT')
