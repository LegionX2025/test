from flask import Blueprint

# Create a blueprint for admin dashboard
admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

# Delay the import of routes to avoid circular import
def register_admin_routes():
    from . import routes  # Import routes inside the function
    routes.setup_admin_routes(admin_blueprint)
