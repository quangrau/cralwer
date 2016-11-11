import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../Functions')

from Helper import Helper

class RestaurantCrawler:

    def __init__(self):
        self.rootURL = 'https://www.foody.vn/ho-chi-minh/'

    def crawl(self, restaurant):
    	url = self.rootURL + restaurant + '/thuc-don'
        html = Helper.parseHTML(url)
        print html
