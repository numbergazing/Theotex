import requests
from bs4 import BeautifulSoup, Tag
from requests import Response

from theotex import SeptuagintBook
from theotex.urls import Book, SEPTUAGINT_CHAPTER, NEW_TESTAMENT_CHAPTER


def nb_chapters_for(book: Book) -> int:

    url: str
    request: Response
    html: BeautifulSoup
    last_chapter_link: Tag

    if type(book) is SeptuagintBook:
        url = SEPTUAGINT_CHAPTER.format(book=book.value, chapter_nb=1)
    else:
        url = NEW_TESTAMENT_CHAPTER.format(book=book.value, chapter_nb=1)

    request = requests.get(url)
    html = BeautifulSoup(request.text, "html.parser")
    last_chapter_link = html.table.table.find_all("tr")[2].find_all("td")[2].find_all("a")[-1]

    return int(last_chapter_link.text)
