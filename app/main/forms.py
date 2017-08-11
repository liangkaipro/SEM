#coding: utf-8
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class QueryForm(Form):
    number = StringField(u'学号',validators = [DataRequired()])
    name = StringField(u'姓名',validators=[DataRequired()])
    submit = SubmitField(u'查询')
