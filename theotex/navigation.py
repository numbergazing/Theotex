import requests
from bs4 import BeautifulSoup, Tag
from requests import Response

from theotex import Book
from theotex.urls import construct_chapter_url


def nb_chapters_for(book: Book) -> int:

    url: str
    request: Response
    html: BeautifulSoup
    last_chapter_link: Tag

    url = construct_chapter_url(book, 1)
    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    last_chapter_link = html.table.table.find_all("tr")[2].find_all("td")[2].find_all("a")[-1]

    return int(last_chapter_link.text)
