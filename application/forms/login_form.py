from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators,SubmitField
from wtforms.validators import ValidationError, InputRequired

# Created a generic custom function that raises a Validation error when the input field is empty.
def fill_form_check(field):
    if len(field.data) <= 0:
        raise ValidationError('Field must be filled')


class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired(), fill_form_check,validators.Length(min=4, max=25)],render_kw={"class": "form-control"})
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Wrong password'),
        fill_form_check],render_kw={"class": "form-control"})
    submit = SubmitField('LOGIN', render_kw={"class": "btn btn-primary form-control-color"})