# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired


class StuinfoForm(Form):
    name = StringField(u'姓名', validators=[DataRequired()])
    number = StringField(u'学号', validators=[DataRequired()])
    grade = StringField(u'年级', validators=[DataRequired()])
    clas = StringField(u'班级', validators=[DataRequired()])


class AssessForm(Form):
    term = SelectField(u'学期', validators=[DataRequired()], choices=[('0', '第一学年上学期'), ('1', '第一学年下学期'),('2', '第二学年上学期'),
                                                                     ('3', '第二学年下学期'), ('4', '第三学年上学期'),('5', '第三学年下学期'),
                                                                     ('6', '第四学年上学期'), ('7', '第四学年下学期'),('8', '第五学年上学期'),
                                                                     ('9', '第五学年下学期'), ('10', '第六学年上学期'),('11','第六学年下学期')])