from flask import Blueprint

# Create a blueprint for auth
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

# Delay the import of routes to avoid circular import
def register_routes():
    from . import routes  # Import routes inside the function
    routes.setup_routes(auth_blueprint)
