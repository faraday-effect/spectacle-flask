from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


user_role = db.Table('user_role',
                     db.Column('user_id', db.ForeignKey('user.id'), primary_key=True),
                     db.Column('role_id', db.ForeignKey('role.id'), primary_key=True))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', secondary=user_role, back_populates='roles')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    roles = db.relationship('Role', secondary=user_role, back_populates='users')

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<Course {}-{}>'.format(self.code, self.name)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.SmallInteger)
    semester = db.Column(db.Enum('Fall', 'Interterm', 'Spring', 'Summer'))
    year = db.Column(db.Integer)
    course = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return '<Section {} {} {} {}>'.format(self.number, self.course.name, self.semester, self.year)
