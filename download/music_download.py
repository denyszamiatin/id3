import requests
import sys
from lxml import html
import random
import re


#sites_with_free_music = ['https://cctrax.com/', 'http://freemusicarchive.org/']

class ParseAndDownload:
    def download(self, url):
        name = random.randrange(1, 99999)
        file_name = str(name) + ".mp3"
        with open(file_name, "wb") as file:
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print
                err
                sys.exit(1)
            file.write(response.content)
        return print('track downloaded')

    def links_parse_xpath(url):
        try:
            page = requests.get(url)
            page.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print
            err
            sys.exit(1)

        tree = html.fromstring(page.content)
        tracks = tree.xpath('//td[@class="song_player"]/a/@download')
        return tracks

    def links_parse_re(url):
        urls = []
        try:
            page = requests.get(url)
            page.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print
            err
            sys.exit(1)
        page = page.text
        regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)\.mp3(?=\")"
        matches = re.finditer(regex, page)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            urls.append(match.group())
        set_urls = set(urls)
        tracks = list(set_urls)
        return tracks


    def iteration(self,tracks):
        for track in tracks:
            self.download(track)
        return 'done'



#url = input("Set url to download ")
#a = ParseAndDownload()
#tracks = a.links_parse_re(url)
#result = a.iteration(tracks)
#print(result)