# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField(u'用户名', Length(1, 64))
    password = PasswordField(u'密码', validators=[DataRequired()])
