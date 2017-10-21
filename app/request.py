from app import app
import urllib.request,json
from .models import news

News = news.News

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
