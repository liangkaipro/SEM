#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_shell_context))
manager.add_command('db', MigrateCommand)

# @manager.command
# def deploy(deploy_type):
#     from app.models import User
#     if deploy_type == 'product':
#         User.insert_admin(username='admin', password='admin')


if __name__ == '__main__':
    manager.run()
