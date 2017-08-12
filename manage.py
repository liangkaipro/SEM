# coding: utf-8
from flask_script import Manager, Shell
from app import create_app, db
from app.models import User
from app import db

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=user)


manager.add_command("shell", shell(make_shell_context))


@manager.command
def deploy(deploy_type):
    from app.models import User

    if deploy_type == 'product':
        User.insert_admin(username='admin', password='admin')


if __name__ == '__main__':
    manager.run()
