# -*- coding: utf-8 -*-
# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, SelectField, RadioField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class StuinfoForm(Form):
    name = StringField(u'姓名', validators=[DataRequired()])
    number = StringField(u'学号', validators=[DataRequired()])
    grade = StringField(u'年级', validators=[DataRequired()])
    clas = StringField(u'班级', validators=[DataRequired()])


class AssessForm(Form):
    term = SelectField(u'学期', validators=[DataRequired()],
                       choices=[('0', '第一学年上学期'), ('1', '第一学年下学期'),
                                ('2', '第二学年上学期'), ('3', '第二学年下学期'),
                                ('4', '第三学年上学期'), ('5', '第三学年下学期'),
                                ('6', '第四学年上学期'), ('7', '第四学年下学期'),
                                ('8', '第五学年上学期'), ('9', '第五学年下学期'),
                                ('10', '第六学年上学期'), ('11', '第六学年下学期')])
    duty = RadioField(u'责任与担当', validators=[DataRequired()],
                      choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    study = RadioField(u'学习与探究', validators=[DataRequired()],
                       choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    health = RadioField(u'健康与生存', validators=[DataRequired()],
                        choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    taste = RadioField(u'审美与人文', validators=[DataRequired()],
                       choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    practice = RadioField(u'实践与创新', validators=[DataRequired()],
                          choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    personality = RadioField(u'个性与发展', validators=[DataRequired()],
                             choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')])
    asses = TextAreaField(u'老师评语', validators=[DataRequired()])


class PluginForm(Form):
    title = StringField(u'标题', validators=[DataRequired()])
    content = TextAreaField(u'内容', validators=[DataRequired()])


class ChangeUserInfoForm(Form):
    username = StringField(u'新用户名', validators=[DataRequired()])
    old_password = PasswordField(u'旧密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[
        DataRequired(), EqualTo('repassword', message=u'两次输入密码不一致！')])
    repassword = PasswordField(u'确认新密码', validators=[DataRequired()])


class AddGradeNavForm(Form):
    name = StringField(u'导航名称', validators=[DataRequired()])
