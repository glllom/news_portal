from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    firstname = StringField("First Name: ", validators=[InputRequired('Please input your name.')])
    lastname = StringField("Last Name: ", validators=[InputRequired('Please input your last name.')])
    password = PasswordField("Password: ", validators=[InputRequired('Please input your password.'),
                                                       Length(min=6, max=16, message="Length must be 6-16 symbols")])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired('Please confirm your password.'),
                                                                       EqualTo('password', 'Passwords do not match.')])
    email = EmailField("Email: ", validators=[InputRequired('Please input your email.'), Email("Email incorrect")])
    country = StringField("Country: ")
    city = StringField("City: ")
    language = StringField("Language: ")
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = EmailField("Email: ", validators=[InputRequired('Please input your email.'), Email("Email incorrect")])
    password = PasswordField("Password: ", validators=[InputRequired('Please input your password.'),
                                                       Length(min=6, max=16, message="Length must be 6-16 symbols")])
    remember = BooleanField('Remember me')
    submit = SubmitField("Log in")


class UpdateInfo(FlaskForm):
    firstname = StringField("First Name: ", validators=[InputRequired('Please input your name.')])
    lastname = StringField("Last Name: ", validators=[InputRequired('Please input your last name.')])
    password = PasswordField("Password: ", validators=[InputRequired('Please input your password.'),
                                                       Length(min=6, max=16, message="Length must be 6-16 symbols")])
    country = StringField("Country: ")
    city = StringField("City: ")
    language = StringField("Language: ")
    submit = SubmitField("Submit")
