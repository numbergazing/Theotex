from typing import List

import requests
from bs4 import BeautifulSoup, Tag, ResultSet
from requests import Response

from exceptions import ChapterDoesNotExistError, VerseDoesNotExistError
from theotex import Book, Verse
from theotex.urls import construct_chapter_url


def _get_markup_for(book: Book, chapter_num: int) -> BeautifulSoup:

    url: str
    request: Response

    url = construct_chapter_url(book, chapter_num)
    request = requests.get(url)
    return BeautifulSoup(request.text, "html.parser")


def _get_filtered_verse_table(html: BeautifulSoup) -> ResultSet:

    verse_rows: ResultSet

    verse_rows = html.body.table.tr.find_all("td")[8].find_all("tr")
    return [row for row in verse_rows if '<div class="num">' in str(row)]


def get_nb_chapters_for(book: Book) -> int:

    html: BeautifulSoup
    last_chapter_link: Tag

    html = _get_markup_for(book, 1)
    last_chapter_link = html.table.table.find_all("tr")[2].find_all("td")[2].find_all("a")[-1]

    return int(last_chapter_link.text)


def get_nb_verses_for(book: Book, chapter_num: int) -> int:

    html: BeautifulSoup

    html = _get_markup_for(book, chapter_num)

    return len(_get_filtered_verse_table(html))


def get_all_verses_for(book: Book, chapter_num: int) -> List[Verse]:

    html: BeautifulSoup
    verse_rows: ResultSet
    verses: List[Verse]

    verses = []
    html = _get_markup_for(book, chapter_num)
    verse_rows = _get_filtered_verse_table(html)

    for row in verse_rows:

        row: Tag
        verse_num: str
        verse_french: str
        verse_greek: str

        verse_num = row.find("div", class_="num").string
        verse_french = row.find("div", class_="vf").text
        verse_greek = row.find("div", class_="vg").text

        verses.append(Verse(book, chapter_num, verse_num, verse_french, verse_greek))

    return verses


def get_verse_for(book: Book, chapter_num: int, verse_ref: str) -> Verse:

    html: BeautifulSoup
    nb_chapters: int
    verse_refs: List[str]
    verse_rows: ResultSet

    nb_chapters = get_nb_chapters_for(book)

    if chapter_num > nb_chapters:
        raise ChapterDoesNotExistError(f"Chapter n° {chapter_num} does not exist for {book.value}")

    html = _get_markup_for(book, chapter_num)
    verse_rows = _get_filtered_verse_table(html)
    verse_refs = [row.find("div", class_="num").string for row in verse_rows]

    if verse_ref not in verse_refs:
        raise VerseDoesNotExistError(f"Verse n° {verse_ref} doesn not exist for chapter {chapter_num} in {book.value}")

    verse_pos = verse_refs.index(verse_ref)
    verse = verse_rows[verse_pos]

    return Verse(book, chapter_num, verse_ref, verse.find("div", class_="vf").text, verse.find("div", class_="vg").text)
