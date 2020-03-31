from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,EqualTo


class RegistrationForm(FlaskForm):
    """Registration form"""
    username =StringField('username_label',
                          validators=[InputRequired(message="Username required"),Length(min=4,max=25,message="Username must be between 4 and 25 characters")])
    password =PasswordField('password_label',
                            validators=[InputRequired(message="Password required"),Length(min=4,max=8,message="Password must be between 4 and 8 characters")])
    confirm_pswd =PasswordField('confirm_pswd_label',
                                validators=[InputRequired(message="Password required"),EqualTo('password',message="passwords must match")])
    salary =PasswordField('salary_label',
                          validators=[InputRequired(message="Salary required"),Length(min=5,max=7,message="Salary must be between 5 and 7 digits")])
    id = PasswordField('id_label')

    submit_button = SubmitField('Create')