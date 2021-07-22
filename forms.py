from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, URL, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL', validators=[URL(), Optional()])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class EditUserForm(FlaskForm):
    """ Form for editing and adding user bio, location, and a header image URL """
    username = StringField('Username')
    email = StringField('E-mail', validators=[Optional(), Email()])
    image_url = StringField('Image URL', validators=[URL(), Optional()])
    location = StringField('Location')
    bio = TextAreaField('Bio')
    header_image_url = StringField('Header Image', validators=[URL(), Optional()])
    password = PasswordField('Password', validators=[Length(min=6), DataRequired()])
