# app/user_dashboard/__init__.py

from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

# Import your routes for the user dashboard
from . import routes  # Assuming you have a routes.py file for user dashboard routes
