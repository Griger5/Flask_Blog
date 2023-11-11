from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Login", validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Hasło", validators=[DataRequired()])
    confirm_password = PasswordField("Powtórz hasło", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Zarejestruj się")

class LoginForm(FlaskForm):
    username = StringField("Login", validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField("Hasło", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się")