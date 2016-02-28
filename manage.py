#!/usr/bin/env python

import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def load():
    """Load sample data."""
    Role.query.delete()
    teacher_role = Role(name='Student')
    db.session.add(teacher_role)
    student_role = Role(name='Teacher')
    db.session.add(student_role)

    User.query.delete()
    teacher1 = User(email='socrates@greece.com')
    teacher1.password = 'pass'
    teacher1.roles = [ teacher_role ]
    db.session.add(teacher1)
    teacher2 = User(email='faraday@london.org')
    teacher2.password = 'pass'
    teacher2.roles = [ teacher_role ]
    db.session.add(teacher2)

    student1 = User(email='cse.student@taylor.edu')
    student1.password = 'pass'
    student1.roles = [ student_role ]
    db.session.add(student1)
    student2 = User(email='art.student@taylor.edu')
    student2.password = 'pass'
    student2.roles = [ student_role ]
    db.session.add(student2)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
