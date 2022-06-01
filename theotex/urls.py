from typing import Union

from theotex import Corpus, SeptuagintBook, NewTestamentBook

HOME = "https://theotex.org"
SEPTUAGINT = f"{HOME}/{Corpus.SEPTUAGINT}"
SEPTUAGINT_CHAPTER = SEPTUAGINT.join("/{book}/{book}_{chapter_nb}.html")
NEW_TESTAMENT = f"{HOME}/{Corpus.NEW_TESTAMENT}"
NEW_TESTAMENT_CHAPTER = NEW_TESTAMENT.join("/{book}/{book}_{chapter_nb}_gf.html")

Book = Union[SeptuagintBook, NewTestamentBook]


def construct_chapter_url(corpus: Corpus, book: Book, chapter: int) -> str:

    url: str

    if corpus is Corpus.SEPTUAGINT:
        url = SEPTUAGINT_CHAPTER
    else:
        url = NEW_TESTAMENT_CHAPTER

    return url.format(book=book.value, chapter_nb=chapter)
