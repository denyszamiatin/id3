"""
Sites with free music https://cctrax.com/, http://freemusicarchive.org/
"""

import random
import re
import os

import requests
from lxml import html


CCTRAX_XPATH = '//td[@class="song_player"]/a/@download'
MP3_RE = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\." \
         r"[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)\.mp3(?=\")"


def _get_unique_filename():
    while True:
        filename = "{}.mp3".format(random.randrange(1, 99999))
        if not os.path.isfile(filename):
            return filename


def _request_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as err:
        print(err)
        return None


def download(url):
    mp3file = _request_url(url)
    if mp3file:
        filename = _get_unique_filename()
        with open(filename, "wb") as file:
            file.write(mp3file.content)


def links_parse_xpath(url, xpath=CCTRAX_XPATH):
    page = _request_url(url).content
    tree = html.fromstring(page)
    return tree.xpath(xpath)


def links_parse_re(url, mp3_re=MP3_RE):
    page = _request_url(url).text
    return {match.group() for match in re.finditer(mp3_re, page)}


def download_tracks(urls):
    for url in urls:
        download(url)


if __name__ == '__main__':
    url = "https://cctrax.com/cousin-silas-the-glove-of-bones/new-dub-manifesto"
    tracks = links_parse_re(url)
    print(tracks)
    download_tracks(tracks)
    print("Ok")