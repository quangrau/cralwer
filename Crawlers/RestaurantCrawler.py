import sys
import os
import csv
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../Functions')

from Functions import *

class RestaurantCrawler:

    def __init__(self, restaurant):
        url = 'https://www.foody.vn/ho-chi-minh/' + restaurant + '/thuc-don'
        html = Helper.parseHTML(url)
        self.soup = BeautifulSoup(html, "lxml")
        self.outputFile = Helper.createFileName()

    def getInfo(self):
        data = []
        dataMetadata = self.getFromMetadata()
        data.extend(dataMetadata)
        Helper.writeInfo(data)

    def getFromMetadata(self):
        longitude = self.soup.find('meta', property='place:location:longitude')
        latitude = self.soup.find('meta', property='place:location:latitude')
        description = self.soup.find('meta', property='og:description')
        name = self.soup.find('h1')

        data = [
                str(name.text.encode('utf8')),
                latitude['content'],
                longitude['content'],
                str(description['content'].encode('utf8'))
            ]

        return data

    def crawl(self):
        self.getInfo()
