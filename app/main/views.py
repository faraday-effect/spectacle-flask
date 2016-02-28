from flask import render_template, flash
from . import main

from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/users')
def users():
    users = db.session.query(User).order_by('email')
    return render_template('users.html', users=users)
