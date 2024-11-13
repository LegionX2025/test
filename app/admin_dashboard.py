from flask import Flask, render_template, request, redirect
from models import Keyword, Source, CrawlerLog, engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/admin_dashboard')
def admin_dashboard():
    keywords = session.query(Keyword).all()
    sources = session.query(Source).all()
    return render_template('admin_dashboard.html', keywords=keywords, sources=sources)

@app.route('/add_keyword', methods=['POST'])
def add_keyword():
    keyword_text = request.form['keyword']
    if keyword_text:
        new_keyword = Keyword(keyword=keyword_text)
        session.add(new_keyword)
        session.commit()
    return redirect('/admin_dashboard')

@app.route('/add_source', methods=['POST'])
def add_source():
    url = request.form['url']
    api_key = request.form.get('api_key')
    description = request.form.get('description', '')
    
    new_source = Source(url=url, api_key=api_key, description=description)
    session.add(new_source)
    session.commit()
    return redirect('/admin_dashboard')
