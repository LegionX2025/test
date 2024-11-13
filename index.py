# main.py
from flask import Flask, render_template
from auth import auth_blueprint
from admin_dashboard import admin_blueprint
from user_dashboard import user_blueprint

app = Flask(__name__)
app.secret_key = "bcd1b7a6cefd92de7e42523d511c7e322b612df6e0534f62"

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(user_blueprint, url_prefix='/user')

@app.route('/')
def landing_page():
    return render_template('landing.html')

# Genezio expects a 'handler' function as the entry point.
# This initializes the app on deployment.
def handler(event=None, context=None):
    return app  # Genezio will call this handler to run the Flask app

# For local testing purposes:
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
