from flask import render_template
from app import app
from .request import get_sources,get_articles_source

# views


@app.route('/')
def index():
    '''
    view root page that returns the landing page and its data
    '''
    general = get_sources('general')
    title = 'Home - Welcome To The Newsroom '
    return render_template('index.html', title=title,general=general)


@app.route('/news/<news_id>')
def news(news_id):
    '''
    news page function that returns the news details page and its data
    '''
    title = 'Welcome To The Newsroom'
    return render_template('news.html', title=title, id=news_id)
