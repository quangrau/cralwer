import sys
import os
import csv
import json
import re
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../Functions')

from Functions import *


class RestaurantCrawler:

    # Constructor
    def __init__(self, restaurant):
        url = 'https://www.foody.vn/can-tho/' + restaurant + '/thuc-don'
        html = Helper.parseHTML(url)
        self.restaurant = restaurant
        self.soup = BeautifulSoup(html, "lxml")

    # Get information from metadata
    def getFromMetadata(self):
        longitude = self.soup.find('meta', property='place:location:longitude')
        latitude = self.soup.find('meta', property='place:location:latitude')
        name = self.soup.find('h1')

        data = [
            str(name.text.encode('utf8')),
            latitude['content'],
            longitude['content'],
        ]

        return data

    # Get position
    def getPosition(self):
        breadCrumList = self.soup.find(
            'span', {'itemtype': 'http://schema.org/BreadcrumbList'})
        position = breadCrumList.findAll('span', {'itemprop': 'name'})
        address = self.soup.find(
            'a', {'href': '/can-tho/' + self.restaurant + '/nearBy'})
        streetAddress = address.find('span')
        print(address, streetAddress)

        data = [
            position[0].text.encode('utf8'),  # Province
            position[1].text.encode('utf8'),  # District
            position[2].text.encode('utf8'),  # Area
            streetAddress.text.encode('utf8')  # Street Address
        ]

        return data

    # Crawling Handler
    def crawl(self):
        data = []
        dataMetadata = self.getFromMetadata()
        dataPosition = self.getPosition()

        data.extend(dataMetadata)
        data.extend(dataPosition)
        Helper.writeInfo(data)
