import requests
from bs4 import BeautifulSoup
from models import CrawlerLog, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()

def crawl_clearweb(url, keywords):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No Title"
    text = soup.get_text()
    
    for keyword in keywords:
        if keyword in text:
            save_log(url, title, text, keyword, source="clearweb")

def crawl_darknet(url, keywords):
    session.proxies.update({'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'})
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No Title"
    text = soup.get_text()

    for keyword in keywords:
        if keyword in text:
            save_log(url, title, text, keyword, source="darknet")

def save_log(url, title, text, keyword, source):
    # Capture details and context with keyword
    log = CrawlerLog(
        url=url,
        title=title,
        description="...",
        date_time=datetime.now(),
        context="...",
        snapshot="...",
        username="...",
        email="...",
        phone="...",
        person_name="...",
        wallet_addresses="..."
    )
    session.add(log)
    session.commit()
