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


@app.route('/news/<id>')
def news(id):
    '''
    news page function that returns the news details page and its data
    '''
    articles = get_articles_source(id)
    title = f'{id}'
    return render_template('news.html', title=title, article = articles)
