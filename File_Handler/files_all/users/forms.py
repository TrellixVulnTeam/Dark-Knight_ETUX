from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, SelectMultipleField, SelectField
from wtforms.fields import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from files_all.models import User, FileContents


class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=40,
                                                                                message="Username can be from 2 to 40 characters longs")])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm Passowrd", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("user name already exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email already exists")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember = BooleanField(label="remember me")
    submit = SubmitField(label='Login')


class NewFileForm(FlaskForm):
    upload = FileField(label="Upload File", validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField(label='Upload')


class ViewFileForm(FlaskForm):
    # check_box_multiple = SelectMultipleField(label="Select_")
    # check_box = SelectField(label="Select")
    start_date = DateField(label='From', format="%Y-%m-%d", id="datepick1", validators=[DataRequired()])
    end_date = DateField(label='To', format="%Y-%m-%d", id="datepick2", validators=[DataRequired()])
    submit = SubmitField(label='Find')

    # TODO check there are records in this time and ensure end is after start date
    def validate(self):
        if self.start_date.data <= self.end_date.data:
            raise ValidationError("End date must be before start date")
