from typing import List

import requests
from bs4 import BeautifulSoup, Tag, ResultSet
from requests import Response

from theotex import Book, Verse
from theotex.urls import construct_chapter_url


def get_nb_chapters_for(book: Book) -> int:

    url: str
    request: Response
    html: BeautifulSoup
    last_chapter_link: Tag

    url = construct_chapter_url(book, 1)
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    last_chapter_link = html.table.table.find_all("tr")[2].find_all("td")[2].find_all("a")[-1]

    return int(last_chapter_link.text)


def get_all_verses_for(book: Book, chapter: int) -> List[Verse]:

    url: str
    request: Response
    html: BeautifulSoup
    verse_rows: ResultSet
    verses: List[Verse]

    verses = []
    url = construct_chapter_url(book, chapter)
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    verse_rows = html.body.table.tr.find_all("td")[8].find_all("tr")

    for row in verse_rows[1:]:

        row: Tag
        verse_num: int
        verse_french: str
        verse_greek: str

        verse_num = int(row.find("div", class_="num").string)
        verse_french = row.find("div", class_="vf").text
        verse_greek = row.find("div", class_="vg").text

        verses.append(Verse(book, chapter, verse_num, verse_french, verse_greek))

    return verses
