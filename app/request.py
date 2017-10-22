from app import app
import urllib.request,json
from .models import news

News = news.New
Article = news.Article

# getting api key
api_key = app.config['NEWS_API_KEY']

#getting base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_results = None

        if get_sources_response['sources']:
            news_results_list = get_sources_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        news_source = News(id,name,description,url,category)
        news_results.append(news_source)




    return news_results

def get_articles_source(id):
    get_articles_url = 'https://newsapi.org/v1/articles?source={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_articles_url)as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    articles_results = []

    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        if publishedAt:
            article_object = Article(author,title,description,url,publishedAt)
            articles_results.append(article_object)

    return articles_results
