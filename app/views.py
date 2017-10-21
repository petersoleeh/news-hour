from flask import render_template
from app import app
from .request import get_sources

# views


@app.route('/')
def index():
    '''
    view root page that returns the landing page and its data
    '''
    business_news = get_sources('business')
    print(business_news)
    title = 'Home - Welcome To The Newsroom '
    return render_template('index.html', title=title,business=business_news)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    news page function that returns the news details page and its data
    '''
    title = 'Welcome To The Newsroom'
    return render_template('news.html', title=title, id=news_id)
