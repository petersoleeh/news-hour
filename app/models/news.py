class News:
    '''
    to define News objects
    '''
    #sources

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

#articles

class Article:

    '''
    to define article objects
    '''

    def __init__(self,author,title,description,url,publishedAt):

        self.author = author
        self.title = title
        self.description =description
        self.url = url
        self.publishedAt = publishedAt
