from flask import Flask, render_template, request, redirect, session
from models import User, engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

Session = sessionmaker(bind=engine)
db_session = Session()

app = Flask(__name__)
app.secret_key = 'bcd1b7a6cefd92de7e42523d511c7e322b612df6e0534f62'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = db_session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect('/user_dashboard')
        else:
            return "Invalid credentials, try again!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')
