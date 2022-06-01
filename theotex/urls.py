from theotex import Corpus

HOME = "https://theotex.org"
SEPTUAGINT = f"{HOME}/{Corpus.SEPTUAGINT}"
SEPTUAGINT_CHAPTER = SEPTUAGINT.join("/{book}/{book}_{chapter_nb}.html")
NEW_TESTAMENT = f"{HOME}/{Corpus.NEW_TESTAMENT}"
NEW_TESTAMENT_CHAPTER = NEW_TESTAMENT.join("/{book}/{book}_{chapter_nb}_gf.html")
