from flask import Flask, render_template, request, Response, stream_with_context
from auth import auth_blueprint
from admin_dashboard import admin_blueprint
from user_dashboard import user_blueprint
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Access environment variables for configuration
app.secret_key = os.environ.get('FLASK_SECRET_KEY')  # Get from env or default value

# Database configuration (PostgreSQL connection string)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://admin:vP0wcNFIG4jo@ep-bold-snow-a64ztnv3-pooler.us-west-2.aws.neon.tech/finalengine?sslmode=require'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources

# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)

# Register blueprints for authentication, admin dashboard, and user dashboard
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
