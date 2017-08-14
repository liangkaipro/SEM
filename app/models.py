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
    number = db.Column(db.Integer, unique=True)
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
    duty = db.Column(db.String(64), unique=True)  # 责任与担当
    study = db.Column(db.String(64), unique=True)  # 学习与探究
    health = db.Column(db.String(64), unique=True)  # 健康与生存
    taste = db.Column(db.String(64), unique=True)  # 审美与人文
    practice = db.Column(db.String(64), unique=True)  # 实践与创新
    pershonality = db.Column(db.String(64), unique=True)  # 个性与发展
    assess = db.Column(db.Text, unique=True)  # 评价
    stuinfo_id = db.Column(db.Integer, db.ForeignKey('stu_info.id'))
    term = db.Column(db.String(64), unique=True)


# 导航表
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)


# 学生信息显示表
class StuInfoView(db.Model):
    __tablename__ = 'stuinfo_view'
    id = db.Column(db.Integer, primary_key=True)
    num_of_view = db.Column(db.BigInteger, default=0)

    @staticmethod
    def insert_view():
        view = StuInfoView(num_of_view=0)
        db.session.add(view)
        db.session.commit()

    @staticmethod
    def add_view(db):
        view = StuInfoView.query.first()
        view.num_of_view += 1
        db.session.add(view)
        db.session.commit()
