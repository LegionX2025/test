# app/user_dashboard/routes.py

from . import user_blueprint
from flask import render_template

@user_blueprint.route('/')
def user_home():
    return render_template('user_home.html')
