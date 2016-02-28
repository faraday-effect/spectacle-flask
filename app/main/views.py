from flask import render_template, flash
from . import main

from .. import db
from ..models import User, Course

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/users')
def users():
    users = db.session.query(User).order_by('email')
    return render_template('users.html', users=users)


@main.route('/courses')
def courses():
    courses = db.session.query(Course).order_by('code')
    return render_template('courses.html', courses=courses)
