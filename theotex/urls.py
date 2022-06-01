from theotex import Corpus, Book, SeptuagintBook

HOME = "https://theotex.org"
SEPTUAGINT = f"{HOME}/{Corpus.SEPTUAGINT.value}"
SEPTUAGINT_CHAPTER = SEPTUAGINT + "/{book}/{book}_{chapter_nb}.html"
NEW_TESTAMENT = f"{HOME}/{Corpus.NEW_TESTAMENT.value}"
NEW_TESTAMENT_CHAPTER = NEW_TESTAMENT + "/{book}/{book}_{chapter_nb}_gf.html"


def construct_chapter_url(book: Book, chapter: int) -> str:

    url: str

    if type(book) is SeptuagintBook:
        return SEPTUAGINT_CHAPTER.format(book=book.value, chapter_nb=chapter)
    else:
        return NEW_TESTAMENT_CHAPTER.format(book=book.value, chapter_nb=chapter)
