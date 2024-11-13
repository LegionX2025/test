# In routes.py, set up the routes for the auth blueprint

def setup_routes(auth_blueprint):
    @auth_blueprint.route('/login')
    def login():
        # Handle login
        return "Login page"

    @auth_blueprint.route('/register')
    def register():
        # Handle registration
        return "Registration page"
