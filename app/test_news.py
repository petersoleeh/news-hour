import unittest
from models import news
News = news.News


class NewsTest(unittest.TestCase):
    '''
    test the behaviour of the News class
    '''

    def setUp(self):
        self.new_news = News("Matthew Hughes", "On-demand delivery app Jinn has permanently shut down.", "It's not clear if Jinn's independent contractors will get the money they're owed.",
                             'https://thenextweb.com/uk/2017/10/19/on-demand-delivery-app-jinn-has-permanently-shut-down', 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/Selection_002-social.png', '2017-10-19T10:13:12Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test__init__(self):
        self.assertEqual(self.new_news.author, "Matthew Hughes")
        self.assertEqual(
            self.new_news.title, "On-demand delivery app Jinn has permanently shut down.")
        self.assertEqual(self.new_news.description,
                         "It's not clear if Jinn's independent contractors will get the money they're owed.")
        self.assertEqual(
            self.new_news.url, 'https://thenextweb.com/uk/2017/10/19/on-demand-delivery-app-jinn-has-permanently-shut-down')
        self.assertEqual(self.new_news.urlToImage,
                         'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/Selection_002-social.png')
        self.assertEqual(self.new_news.publishedAt, '2017-10-19T10:13:12Z')


if __name__ == '__main__':
    unittest.main(verbosity=2)
