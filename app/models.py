# -*- coding: utf-8 -*-
from flask_login import UserMixin
from app import db, login_manager


# 管理员用户表
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))

    @staticmethod
    def insert_admin(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 学生信息表
class StuInfo(db.Model):
    __tablename__ = 'stu_info'
    id = db.Column(db.Integer, primary_key=True)
    stu_name = db.Column(db.String(64), unique=True)
    grade = db.Column(db.String(64), unique=True)
    cla = db.Column(db.String(64), unique=True)
    assess = db.relationship('Assess', backref='stu_info')


# 公告表
class Plugin(db.Model):
    __tablename__ = 'plugin'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    note = db.Column(db.Text, default='')
    content = db.Column(db.Text, default='')
    order = db.Column(db.Integer, default=0)
    disable = db.Column(db.Boolean, default=False)

    @staticmethod
    def insert_system_plugin():
        plugin = Plugin(title=u'公告',
                        note=u'系统信息',
                        content='system',
                        order=1)
        db.session.add(plugin)
        db.session.commit()

    def sort_delete(self):
        for plugin in Plugin.query.order_by(Plugin.order.asc()).offset(self.order).all():
            plugin.order -= 1
            db.session.add(plugin)

    def __repr__(self):
        return '<Plugin %r>' % self.title


# 评价信息表
class Assess(db.Model):
    __tablename__ = 'assess'
    id = db.Column(db.Integer, primary_key=True)
    zeren = db.Column(db.String(64), unique=True)
    xuexi = db.Column(db.String(64), unique=True)
    jiankang = db.Column(db.String(64), unique=True)
    shenmei = db.Column(db.String(64), unique=True)
    shijian = db.Column(db.String(64), unique=True)
    gexing = db.Column(db.String(64), unique=True)
    stuinfo_id = db.Column(db.Integer, db.ForeignKey('stuinfo.id'))
    term = db.Column(db.String(64), unique=True)


# 导航表
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
