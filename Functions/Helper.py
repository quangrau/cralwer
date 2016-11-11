import requests
import time

class Helper:

    @staticmethod
    def parseHTML(link):
        try:
            html = requests.get(link)
        except Exception, e:
            time.sleep(1)
            html = requests.get(link)
        return html.content
