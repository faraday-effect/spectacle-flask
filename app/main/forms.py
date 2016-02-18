from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    email = StringField('Email Address', validators=[Required()])
    password = StringField('Password', validators=[Required()])
