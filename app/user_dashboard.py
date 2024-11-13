@app.route('/user_dashboard')
def user_dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    
    user_keywords = session.query(Keyword).all()  # Customize based on user
    logs = session.query(CrawlerLog).all()  # Display all logs or filter by user preferences
    return render_template('user_dashboard.html', keywords=user_keywords, logs=logs)
