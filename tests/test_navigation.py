from logs import debug_log
from theotex import SeptuagintBook, NewTestamentBook

from navigation import get_nb_chapters_for, get_all_verses_for, get_nb_verses_for, get_verse_for, get_verses_for, \
    _get_book_greek_name, _get_markup_for


def test_nb_chapters_for() -> None:
    expected_result = [50, 28]
    data = [get_nb_chapters_for(SeptuagintBook.genese), get_nb_chapters_for(NewTestamentBook.matthieu)]
    assert data == expected_result


def test_get_nb_verses_for() -> None:
    expected_result = [31, 25]
    data = [get_nb_verses_for(SeptuagintBook.genese, 1), get_nb_verses_for(NewTestamentBook.matthieu, 1)]
    assert data == expected_result


def test_get_all_verses_for() -> None:
    expected_result = [
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "1",
            "french_version": "Au commencement Dieu cr\u00e9a le ciel et la terre.",
            "greek_version": "\u1f18\u03bd \u1f00\u03c1\u03c7\u1fc7 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78\u03bd \u03bf\u1f50\u03c1\u03b1\u03bd\u1f78\u03bd \u03ba\u03b1\u1f76 \u03c4\u1f74\u03bd \u03b3\u1fc6\u03bd."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "2",
            "french_version": "Or la terre \u00e9tait invisible et vide\u2009; les t\u00e9n\u00e8bres \u00e9taient au-dessus de l'ab\u00eeme, et l'Esprit de Dieu \u00e9tait port\u00e9 sur les eaux.",
            "greek_version": "\u1f21 \u03b4\u1f72 \u03b3\u1fc6 \u1f26\u03bd \u1f00\u1f79\u03c1\u03b1\u03c4\u03bf\u03c2 \u03ba\u03b1\u1f76 \u1f00\u03ba\u03b1\u03c4\u03b1\u03c3\u03ba\u03b5\u1f7b\u03b1\u03c3\u03c4\u03bf\u03c2, \u03ba\u03b1\u1f76 \u03c3\u03ba\u1f79\u03c4\u03bf\u03c2 \u1f10\u03c0\u1f71\u03bd\u03c9 \u03c4\u1fc6\u03c2 \u1f00\u03b2\u1f7b\u03c3\u03c3\u03bf\u03c5, \u03ba\u03b1\u1f76 \u03c0\u03bd\u03b5\u1fe6\u03bc\u03b1 \u03b8\u03b5\u03bf\u1fe6 \u1f10\u03c0\u03b5\u03c6\u1f73\u03c1\u03b5\u03c4\u03bf \u1f10\u03c0\u1f71\u03bd\u03c9 \u03c4\u03bf\u1fe6 \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "3",
            "french_version": "Et Dieu dit\u2009: Soit la lumi\u00e8re, et la lumi\u00e8re fut.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u0393\u03b5\u03bd\u03b7\u03b8\u1f75\u03c4\u03c9 \u03c6\u1ff6\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c6\u1ff6\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "4",
            "french_version": "Dieu vit que la lumi\u00e8re \u00e9tait bonne, et il s\u00e9para la lumi\u00e8re des t\u00e9n\u00e8bres.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78 \u03c6\u1ff6\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd. \u03ba\u03b1\u1f76 \u03b4\u03b9\u03b5\u03c7\u1f7d\u03c1\u03b9\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u03c6\u03c9\u03c4\u1f78\u03c2 \u03ba\u03b1\u1f76 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u03c3\u03ba\u1f79\u03c4\u03bf\u03c5\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "5",
            "french_version": "Dieu appela la lumi\u00e8re jour\u2009; il appela nuit les t\u00e9n\u00e8bres. Et il y eut un soir, et il y eut un matin\u2009; un jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78 \u03c6\u1ff6\u03c2 \u1f21\u03bc\u1f73\u03c1\u03b1\u03bd \u03ba\u03b1\u1f76 \u03c4\u1f78 \u03c3\u03ba\u1f79\u03c4\u03bf\u03c2 \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u03bd\u1f7b\u03ba\u03c4\u03b1. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u03bc\u1f77\u03b1."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "6",
            "french_version": "Dieu dit ensuite\u2009: Qu'il y ait un firmament au milieu des eaux\u2009; qu'il s\u00e9pare les eaux des eaux\u2009; et il en fut ainsi.",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u0393\u03b5\u03bd\u03b7\u03b8\u1f75\u03c4\u03c9 \u03c3\u03c4\u03b5\u03c1\u1f73\u03c9\u03bc\u03b1 \u1f10\u03bd \u03bc\u1f73\u03c3\u1ff3 \u03c4\u03bf\u1fe6 \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2 \u03ba\u03b1\u1f76 \u1f14\u03c3\u03c4\u03c9 \u03b4\u03b9\u03b1\u03c7\u03c9\u03c1\u1f77\u03b6\u03bf\u03bd \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2 \u03ba\u03b1\u1f76 \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "7",
            "french_version": "Dieu cr\u00e9a le firmament, il s\u00e9para les eaux qui \u00e9taient au-dessus du firmament, des eaux qui \u00e9taient au-dessous du firmament.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78 \u03c3\u03c4\u03b5\u03c1\u1f73\u03c9\u03bc\u03b1, \u03ba\u03b1\u1f76 \u03b4\u03b9\u03b5\u03c7\u1f7d\u03c1\u03b9\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2, \u1f43 \u1f26\u03bd \u1f51\u03c0\u03bf\u03ba\u1f71\u03c4\u03c9 \u03c4\u03bf\u1fe6 \u03c3\u03c4\u03b5\u03c1\u03b5\u1f7d\u03bc\u03b1\u03c4\u03bf\u03c2, \u03ba\u03b1\u1f76 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u1f55\u03b4\u03b1\u03c4\u03bf\u03c2 \u03c4\u03bf\u1fe6 \u1f10\u03c0\u1f71\u03bd\u03c9 \u03c4\u03bf\u1fe6 \u03c3\u03c4\u03b5\u03c1\u03b5\u1f7d\u03bc\u03b1\u03c4\u03bf\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "8",
            "french_version": "Il appela le firmament ciel. Et Dieu vit que cela \u00e9tait bien. Et il y eut un soir, et il y eut un matin, et ce fut un deuxi\u00e8me jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78 \u03c3\u03c4\u03b5\u03c1\u1f73\u03c9\u03bc\u03b1 \u03bf\u1f50\u03c1\u03b1\u03bd\u1f79\u03bd. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u03b4\u03b5\u03c5\u03c4\u1f73\u03c1\u03b1."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "9",
            "french_version": "Apr\u00e8s quoi Dieu dit\u2009: Que les eaux, au-dessous du ciel, soient r\u00e9unies en un seul amas, et que l'aride apparaisse. Et il en fut ainsi\u2009: les eaux, au-dessous du ciel, furent r\u00e9unies en un seul amas, et l'aride apparut.",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u03a3\u03c5\u03bd\u03b1\u03c7\u03b8\u1f75\u03c4\u03c9 \u03c4\u1f78 \u1f55\u03b4\u03c9\u03c1 \u03c4\u1f78 \u1f51\u03c0\u03bf\u03ba\u1f71\u03c4\u03c9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03b5\u1f30\u03c2 \u03c3\u03c5\u03bd\u03b1\u03b3\u03c9\u03b3\u1f74\u03bd \u03bc\u1f77\u03b1\u03bd, \u03ba\u03b1\u1f76 \u1f40\u03c6\u03b8\u1f75\u03c4\u03c9 \u1f21 \u03be\u03b7\u03c1\u1f71. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2. \u03ba\u03b1\u1f76 \u03c3\u03c5\u03bd\u1f75\u03c7\u03b8\u03b7 \u03c4\u1f78 \u1f55\u03b4\u03c9\u03c1 \u03c4\u1f78 \u1f51\u03c0\u03bf\u03ba\u1f71\u03c4\u03c9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03b5\u1f30\u03c2 \u03c4\u1f70\u03c2 \u03c3\u03c5\u03bd\u03b1\u03b3\u03c9\u03b3\u1f70\u03c2 \u03b1\u1f50\u03c4\u1ff6\u03bd, \u03ba\u03b1\u1f76 \u1f64\u03c6\u03b8\u03b7 \u1f21 \u03be\u03b7\u03c1\u1f71."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "10",
            "french_version": "Dieu appela l'aride terre\u2009; il appela mers l'amas des eaux. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f74\u03bd \u03be\u03b7\u03c1\u1f70\u03bd \u03b3\u1fc6\u03bd \u03ba\u03b1\u1f76 \u03c4\u1f70 \u03c3\u03c5\u03c3\u03c4\u1f75\u03bc\u03b1\u03c4\u03b1 \u03c4\u1ff6\u03bd \u1f51\u03b4\u1f71\u03c4\u03c9\u03bd \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u03b8\u03b1\u03bb\u1f71\u03c3\u03c3\u03b1\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "11",
            "french_version": "Et Dieu dit\u2009: Que la terre produise des plantes herbac\u00e9es, portant semence selon les esp\u00e8ces et les similitudes, et des arbres fertiles en fruits, qui aient en eux les semences propres \u00e0 chaque esp\u00e8ce sur la terre. Et il en fut ainsi\u2009:",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u0392\u03bb\u03b1\u03c3\u03c4\u03b7\u03c3\u1f71\u03c4\u03c9 \u1f21 \u03b3\u1fc6 \u03b2\u03bf\u03c4\u1f71\u03bd\u03b7\u03bd \u03c7\u1f79\u03c1\u03c4\u03bf\u03c5, \u03c3\u03c0\u03b5\u1fd6\u03c1\u03bf\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03ba\u03b1\u03b8 \u1f41\u03bc\u03bf\u03b9\u1f79\u03c4\u03b7\u03c4\u03b1, \u03ba\u03b1\u1f76 \u03be\u1f7b\u03bb\u03bf\u03bd \u03ba\u1f71\u03c1\u03c0\u03b9\u03bc\u03bf\u03bd \u03c0\u03bf\u03b9\u03bf\u1fe6\u03bd \u03ba\u03b1\u03c1\u03c0\u1f79\u03bd, \u03bf\u1f57 \u03c4\u1f78 \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03b1\u1f50\u03c4\u03bf\u1fe6 \u1f10\u03bd \u03b1\u1f50\u03c4\u1ff7 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "12",
            "french_version": "La terre produisit des plantes herbac\u00e9es, portant semence selon les esp\u00e8ces et les similitudes, et des arbres fertiles en fruits ayant en eux les semences propres \u00e0 chaque esp\u00e8ce sur la terre. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03be\u1f75\u03bd\u03b5\u03b3\u03ba\u03b5\u03bd \u1f21 \u03b3\u1fc6 \u03b2\u03bf\u03c4\u1f71\u03bd\u03b7\u03bd \u03c7\u1f79\u03c1\u03c4\u03bf\u03c5, \u03c3\u03c0\u03b5\u1fd6\u03c1\u03bf\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03ba\u03b1\u03b8 \u1f41\u03bc\u03bf\u03b9\u1f79\u03c4\u03b7\u03c4\u03b1, \u03ba\u03b1\u1f76 \u03be\u1f7b\u03bb\u03bf\u03bd \u03ba\u1f71\u03c1\u03c0\u03b9\u03bc\u03bf\u03bd \u03c0\u03bf\u03b9\u03bf\u1fe6\u03bd \u03ba\u03b1\u03c1\u03c0\u1f79\u03bd, \u03bf\u1f57 \u03c4\u1f78 \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03b1\u1f50\u03c4\u03bf\u1fe6 \u1f10\u03bd \u03b1\u1f50\u03c4\u1ff7 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "13",
            "french_version": "Et il y eut un soir, et il y eut un matin, et ce fut un troisi\u00e8me jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u03c4\u03c1\u1f77\u03c4\u03b7."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "14",
            "french_version": "Dieu dit ensuite\u2009: Que des luminaires soient dans le firmament du ciel, pour luire sur la terre et s\u00e9parer les jours et les nuits\u2009; qu'ils soient les signes des temps et des jours et des ann\u00e9es\u2009;",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u0393\u03b5\u03bd\u03b7\u03b8\u1f75\u03c4\u03c9\u03c3\u03b1\u03bd \u03c6\u03c9\u03c3\u03c4\u1fc6\u03c1\u03b5\u03c2 \u1f10\u03bd \u03c4\u1ff7 \u03c3\u03c4\u03b5\u03c1\u03b5\u1f7d\u03bc\u03b1\u03c4\u03b9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03b5\u1f30\u03c2 \u03c6\u03b1\u1fe6\u03c3\u03b9\u03bd \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03c4\u03bf\u1fe6 \u03b4\u03b9\u03b1\u03c7\u03c9\u03c1\u1f77\u03b6\u03b5\u03b9\u03bd \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u1fc6\u03c2 \u1f21\u03bc\u1f73\u03c1\u03b1\u03c2 \u03ba\u03b1\u1f76 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u1fc6\u03c2 \u03bd\u03c5\u03ba\u03c4\u1f78\u03c2 \u03ba\u03b1\u1f76 \u1f14\u03c3\u03c4\u03c9\u03c3\u03b1\u03bd \u03b5\u1f30\u03c2 \u03c3\u03b7\u03bc\u03b5\u1fd6\u03b1 \u03ba\u03b1\u1f76 \u03b5\u1f30\u03c2 \u03ba\u03b1\u03b9\u03c1\u03bf\u1f7a\u03c2 \u03ba\u03b1\u1f76 \u03b5\u1f30\u03c2 \u1f21\u03bc\u1f73\u03c1\u03b1\u03c2 \u03ba\u03b1\u1f76 \u03b5\u1f30\u03c2 \u1f10\u03bd\u03b9\u03b1\u03c5\u03c4\u03bf\u1f7a\u03c2"
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "15",
            "french_version": "Qu'ils brillent au firmament du ciel, pour \u00e9clairer la surface de la terre. Et il en fut ainsi\u2009:",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f14\u03c3\u03c4\u03c9\u03c3\u03b1\u03bd \u03b5\u1f30\u03c2 \u03c6\u03b1\u1fe6\u03c3\u03b9\u03bd \u1f10\u03bd \u03c4\u1ff7 \u03c3\u03c4\u03b5\u03c1\u03b5\u1f7d\u03bc\u03b1\u03c4\u03b9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u1f65\u03c3\u03c4\u03b5 \u03c6\u03b1\u1f77\u03bd\u03b5\u03b9\u03bd \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "16",
            "french_version": "Dieu cr\u00e9a les deux grands luminaires\u2009: le plus grand luminaire pour pr\u00e9sider aux jours, le luminaire le plus petit pour pr\u00e9sider aux nuits. Il cr\u00e9a les \u00e9toiles,",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u03bf\u1f7a\u03c2 \u03b4\u1f7b\u03bf \u03c6\u03c9\u03c3\u03c4\u1fc6\u03c1\u03b1\u03c2 \u03c4\u03bf\u1f7a\u03c2 \u03bc\u03b5\u03b3\u1f71\u03bb\u03bf\u03c5\u03c2, \u03c4\u1f78\u03bd \u03c6\u03c9\u03c3\u03c4\u1fc6\u03c1\u03b1 \u03c4\u1f78\u03bd \u03bc\u1f73\u03b3\u03b1\u03bd \u03b5\u1f30\u03c2 \u1f00\u03c1\u03c7\u1f70\u03c2 \u03c4\u1fc6\u03c2 \u1f21\u03bc\u1f73\u03c1\u03b1\u03c2 \u03ba\u03b1\u1f76 \u03c4\u1f78\u03bd \u03c6\u03c9\u03c3\u03c4\u1fc6\u03c1\u03b1 \u03c4\u1f78\u03bd \u1f10\u03bb\u1f71\u03c3\u03c3\u03c9 \u03b5\u1f30\u03c2 \u1f00\u03c1\u03c7\u1f70\u03c2 \u03c4\u1fc6\u03c2 \u03bd\u03c5\u03ba\u03c4\u1f79\u03c2, \u03ba\u03b1\u1f76 \u03c4\u03bf\u1f7a\u03c2 \u1f00\u03c3\u03c4\u1f73\u03c1\u03b1\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "17",
            "french_version": "Qu'il pla\u00e7a dans le firmament du ciel pour \u00e9clairer la surface de la terre,",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f14\u03b8\u03b5\u03c4\u03bf \u03b1\u1f50\u03c4\u03bf\u1f7a\u03c2 \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f10\u03bd \u03c4\u1ff7 \u03c3\u03c4\u03b5\u03c1\u03b5\u1f7d\u03bc\u03b1\u03c4\u03b9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u1f65\u03c3\u03c4\u03b5 \u03c6\u03b1\u1f77\u03bd\u03b5\u03b9\u03bd \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2"
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "18",
            "french_version": "Pr\u00e9sider aux jours et aux nuits, et s\u00e9parer la lumi\u00e8re des t\u00e9n\u00e8bres. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f04\u03c1\u03c7\u03b5\u03b9\u03bd \u03c4\u1fc6\u03c2 \u1f21\u03bc\u1f73\u03c1\u03b1\u03c2 \u03ba\u03b1\u1f76 \u03c4\u1fc6\u03c2 \u03bd\u03c5\u03ba\u03c4\u1f78\u03c2 \u03ba\u03b1\u1f76 \u03b4\u03b9\u03b1\u03c7\u03c9\u03c1\u1f77\u03b6\u03b5\u03b9\u03bd \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u03c6\u03c9\u03c4\u1f78\u03c2 \u03ba\u03b1\u1f76 \u1f00\u03bd\u1f70 \u03bc\u1f73\u03c3\u03bf\u03bd \u03c4\u03bf\u1fe6 \u03c3\u03ba\u1f79\u03c4\u03bf\u03c5\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "19",
            "french_version": "Et il y eut un soir, et il y eut un matin, et ce fut un quatri\u00e8me jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u03c4\u03b5\u03c4\u1f71\u03c1\u03c4\u03b7."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "20",
            "french_version": "Et Dieu dit\u2009: Que les eaux produisent des reptiles, \u00e2mes vivantes, et des oiseaux volant sur la terre, sous le firmament du ciel. Et il en fut ainsi\u2009:",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u1f18\u03be\u03b1\u03b3\u03b1\u03b3\u1f73\u03c4\u03c9 \u03c4\u1f70 \u1f55\u03b4\u03b1\u03c4\u03b1 \u1f11\u03c1\u03c0\u03b5\u03c4\u1f70 \u03c8\u03c5\u03c7\u1ff6\u03bd \u03b6\u03c9\u03c3\u1ff6\u03bd \u03ba\u03b1\u1f76 \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u1f70 \u03c0\u03b5\u03c4\u1f79\u03bc\u03b5\u03bd\u03b1 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u03c4\u1f70 \u03c4\u1f78 \u03c3\u03c4\u03b5\u03c1\u1f73\u03c9\u03bc\u03b1 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "21",
            "french_version": "Dieu cr\u00e9a les grands poissons, et tout reptile (\u00e2me vivante) que les eaux produisirent par esp\u00e8ces. Il cr\u00e9a tous les oiseaux ail\u00e9s par esp\u00e8ces. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f70 \u03ba\u1f75\u03c4\u03b7 \u03c4\u1f70 \u03bc\u03b5\u03b3\u1f71\u03bb\u03b1 \u03ba\u03b1\u1f76 \u03c0\u1fb6\u03c3\u03b1\u03bd \u03c8\u03c5\u03c7\u1f74\u03bd \u03b6\u1ff4\u03c9\u03bd \u1f11\u03c1\u03c0\u03b5\u03c4\u1ff6\u03bd, \u1f03 \u1f10\u03be\u1f75\u03b3\u03b1\u03b3\u03b5\u03bd \u03c4\u1f70 \u1f55\u03b4\u03b1\u03c4\u03b1 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03b7 \u03b1\u1f50\u03c4\u1ff6\u03bd, \u03ba\u03b1\u1f76 \u03c0\u1fb6\u03bd \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u1f78\u03bd \u03c0\u03c4\u03b5\u03c1\u03c9\u03c4\u1f78\u03bd \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f71."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "22",
            "french_version": "Puis Dieu les b\u00e9nit, disant\u2009: Croissez et multipliez, remplissez les eaux des mers\u2009; et que les oiseaux multiplient sur la terre.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b7\u1f50\u03bb\u1f79\u03b3\u03b7\u03c3\u03b5\u03bd \u03b1\u1f50\u03c4\u1f70 \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03bb\u1f73\u03b3\u03c9\u03bd \u0391\u1f50\u03be\u1f71\u03bd\u03b5\u03c3\u03b8\u03b5 \u03ba\u03b1\u1f76 \u03c0\u03bb\u03b7\u03b8\u1f7b\u03bd\u03b5\u03c3\u03b8\u03b5 \u03ba\u03b1\u1f76 \u03c0\u03bb\u03b7\u03c1\u1f7d\u03c3\u03b1\u03c4\u03b5 \u03c4\u1f70 \u1f55\u03b4\u03b1\u03c4\u03b1 \u1f10\u03bd \u03c4\u03b1\u1fd6\u03c2 \u03b8\u03b1\u03bb\u1f71\u03c3\u03c3\u03b1\u03b9\u03c2, \u03ba\u03b1\u1f76 \u03c4\u1f70 \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u1f70 \u03c0\u03bb\u03b7\u03b8\u03c5\u03bd\u1f73\u03c3\u03b8\u03c9\u03c3\u03b1\u03bd \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "23",
            "french_version": "Et il y eut un soir, et il y eut un matin, et ce fut un cinqui\u00e8me jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u03c0\u1f73\u03bc\u03c0\u03c4\u03b7."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "24",
            "french_version": "Dieu dit ensuite\u2009: Que la terre produise des \u00e2mes vivantes, selon les esp\u00e8ces\u2009: quadrup\u00e8des, reptiles, b\u00eates fauves de la terre, par esp\u00e8ces. Et il en fut ainsi\u2009:",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u1f18\u03be\u03b1\u03b3\u03b1\u03b3\u1f73\u03c4\u03c9 \u1f21 \u03b3\u1fc6 \u03c8\u03c5\u03c7\u1f74\u03bd \u03b6\u1ff6\u03c3\u03b1\u03bd \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2, \u03c4\u03b5\u03c4\u03c1\u1f71\u03c0\u03bf\u03b4\u03b1 \u03ba\u03b1\u1f76 \u1f11\u03c1\u03c0\u03b5\u03c4\u1f70 \u03ba\u03b1\u1f76 \u03b8\u03b7\u03c1\u1f77\u03b1 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "25",
            "french_version": "Dieu cr\u00e9a les b\u00eates fauves de la terre, par esp\u00e8ces, les bestiaux selon leurs esp\u00e8ces, et tous les reptiles de la terre par esp\u00e8ces. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f70 \u03b8\u03b7\u03c1\u1f77\u03b1 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03c4\u1f70 \u03ba\u03c4\u1f75\u03bd\u03b7 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03c0\u1f71\u03bd\u03c4\u03b1 \u03c4\u1f70 \u1f11\u03c1\u03c0\u03b5\u03c4\u1f70 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03b1\u1f50\u03c4\u1ff6\u03bd. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f71."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "26",
            "french_version": "Alors Dieu dit\u2009: Cr\u00e9ons l'homme \u00e0 notre image et ressemblance, qu'il ait tout pouvoir sur les poissons de la mer, sur les oiseaux du ciel, et sur les bestiaux, et sur toute la terre, et sur les reptiles se tra\u00eenant \u00e0 terre.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u03a0\u03bf\u03b9\u1f75\u03c3\u03c9\u03bc\u03b5\u03bd \u1f04\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03bd \u03ba\u03b1\u03c4 \u03b5\u1f30\u03ba\u1f79\u03bd\u03b1 \u1f21\u03bc\u03b5\u03c4\u1f73\u03c1\u03b1\u03bd \u03ba\u03b1\u1f76 \u03ba\u03b1\u03b8 \u1f41\u03bc\u03bf\u1f77\u03c9\u03c3\u03b9\u03bd, \u03ba\u03b1\u1f76 \u1f00\u03c1\u03c7\u1f73\u03c4\u03c9\u03c3\u03b1\u03bd \u03c4\u1ff6\u03bd \u1f30\u03c7\u03b8\u1f7b\u03c9\u03bd \u03c4\u1fc6\u03c2 \u03b8\u03b1\u03bb\u1f71\u03c3\u03c3\u03b7\u03c2 \u03ba\u03b1\u1f76 \u03c4\u1ff6\u03bd \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u1ff6\u03bd \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03ba\u03b1\u1f76 \u03c4\u1ff6\u03bd \u03ba\u03c4\u03b7\u03bd\u1ff6\u03bd \u03ba\u03b1\u1f76 \u03c0\u1f71\u03c3\u03b7\u03c2 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u1f76 \u03c0\u1f71\u03bd\u03c4\u03c9\u03bd \u03c4\u1ff6\u03bd \u1f11\u03c1\u03c0\u03b5\u03c4\u1ff6\u03bd \u03c4\u1ff6\u03bd \u1f11\u03c1\u03c0\u1f79\u03bd\u03c4\u03c9\u03bd \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "27",
            "french_version": "Et Dieu cr\u00e9a l'homme\u2009; il le cr\u00e9a \u00e0 l'image de Dieu\u2009; il les cr\u00e9a m\u00e2le et femelle.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78\u03bd \u1f04\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03bd, \u03ba\u03b1\u03c4 \u03b5\u1f30\u03ba\u1f79\u03bd\u03b1 \u03b8\u03b5\u03bf\u1fe6 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u03b1\u1f50\u03c4\u1f79\u03bd, \u1f04\u03c1\u03c3\u03b5\u03bd \u03ba\u03b1\u1f76 \u03b8\u1fc6\u03bb\u03c5 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u03b1\u1f50\u03c4\u03bf\u1f7b\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "28",
            "french_version": "Et Dieu les b\u00e9nit, disant\u2009: Croissez et multipliez, remplissez la terre, et dominez sur elle\u2009; soyez ma\u00eetres des poissons de la mer, et des oiseaux du ciel, et de tous les bestiaux, et de toute la terre, et de tous les reptiles qui se tra\u00eenent \u00e0 terre.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b7\u1f50\u03bb\u1f79\u03b3\u03b7\u03c3\u03b5\u03bd \u03b1\u1f50\u03c4\u03bf\u1f7a\u03c2 \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03bb\u1f73\u03b3\u03c9\u03bd \u0391\u1f50\u03be\u1f71\u03bd\u03b5\u03c3\u03b8\u03b5 \u03ba\u03b1\u1f76 \u03c0\u03bb\u03b7\u03b8\u1f7b\u03bd\u03b5\u03c3\u03b8\u03b5 \u03ba\u03b1\u1f76 \u03c0\u03bb\u03b7\u03c1\u1f7d\u03c3\u03b1\u03c4\u03b5 \u03c4\u1f74\u03bd \u03b3\u1fc6\u03bd \u03ba\u03b1\u1f76 \u03ba\u03b1\u03c4\u03b1\u03ba\u03c5\u03c1\u03b9\u03b5\u1f7b\u03c3\u03b1\u03c4\u03b5 \u03b1\u1f50\u03c4\u1fc6\u03c2 \u03ba\u03b1\u1f76 \u1f04\u03c1\u03c7\u03b5\u03c4\u03b5 \u03c4\u1ff6\u03bd \u1f30\u03c7\u03b8\u1f7b\u03c9\u03bd \u03c4\u1fc6\u03c2 \u03b8\u03b1\u03bb\u1f71\u03c3\u03c3\u03b7\u03c2 \u03ba\u03b1\u1f76 \u03c4\u1ff6\u03bd \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u1ff6\u03bd \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03ba\u03b1\u1f76 \u03c0\u1f71\u03bd\u03c4\u03c9\u03bd \u03c4\u1ff6\u03bd \u03ba\u03c4\u03b7\u03bd\u1ff6\u03bd \u03ba\u03b1\u1f76 \u03c0\u1f71\u03c3\u03b7\u03c2 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u1f76 \u03c0\u1f71\u03bd\u03c4\u03c9\u03bd \u03c4\u1ff6\u03bd \u1f11\u03c1\u03c0\u03b5\u03c4\u1ff6\u03bd \u03c4\u1ff6\u03bd \u1f11\u03c1\u03c0\u1f79\u03bd\u03c4\u03c9\u03bd \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "29",
            "french_version": "Voyez, dit Dieu, je vous donne toutes les plantes \u00e0 semence qui germent \u00e0 la surface de la terre\u2009; que tous les arbres qui portent des fruits \u00e0 semence soient \u00e0 vous, pour \u00eatre votre nourriture.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u1f38\u03b4\u03bf\u1f7a \u03b4\u1f73\u03b4\u03c9\u03ba\u03b1 \u1f51\u03bc\u1fd6\u03bd \u03c0\u1fb6\u03bd \u03c7\u1f79\u03c1\u03c4\u03bf\u03bd \u03c3\u03c0\u1f79\u03c1\u03b9\u03bc\u03bf\u03bd \u03c3\u03c0\u03b5\u1fd6\u03c1\u03bf\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1, \u1f45 \u1f10\u03c3\u03c4\u03b9\u03bd \u1f10\u03c0\u1f71\u03bd\u03c9 \u03c0\u1f71\u03c3\u03b7\u03c2 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2, \u03ba\u03b1\u1f76 \u03c0\u1fb6\u03bd \u03be\u1f7b\u03bb\u03bf\u03bd, \u1f43 \u1f14\u03c7\u03b5\u03b9 \u1f10\u03bd \u1f11\u03b1\u03c5\u03c4\u1ff7 \u03ba\u03b1\u03c1\u03c0\u1f78\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c0\u03bf\u03c1\u1f77\u03bc\u03bf\u03c5 \u2013 \u1f51\u03bc\u1fd6\u03bd \u1f14\u03c3\u03c4\u03b1\u03b9 \u03b5\u1f30\u03c2 \u03b2\u03c1\u1ff6\u03c3\u03b9\u03bd"
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "30",
            "french_version": "Que toutes les b\u00eates fauves de la terre, tous les oiseaux du ciel, tous les reptiles qui se tra\u00eenent \u00e0 terre, et ont en eux une \u00e2me vivante, aient pour nourriture toute herbe verdoyante. Et il en fut ainsi.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03c0\u1fb6\u03c3\u03b9 \u03c4\u03bf\u1fd6\u03c2 \u03b8\u03b7\u03c1\u1f77\u03bf\u03b9\u03c2 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2 \u03ba\u03b1\u1f76 \u03c0\u1fb6\u03c3\u03b9 \u03c4\u03bf\u1fd6\u03c2 \u03c0\u03b5\u03c4\u03b5\u03b9\u03bd\u03bf\u1fd6\u03c2 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03ba\u03b1\u1f76 \u03c0\u03b1\u03bd\u03c4\u1f76 \u1f11\u03c1\u03c0\u03b5\u03c4\u1ff7 \u03c4\u1ff7 \u1f15\u03c1\u03c0\u03bf\u03bd\u03c4\u03b9 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2, \u1f43 \u1f14\u03c7\u03b5\u03b9 \u1f10\u03bd \u1f11\u03b1\u03c5\u03c4\u1ff7 \u03c8\u03c5\u03c7\u1f74\u03bd \u03b6\u03c9\u1fc6\u03c2, \u03c0\u1f71\u03bd\u03c4\u03b1 \u03c7\u1f79\u03c1\u03c4\u03bf\u03bd \u03c7\u03bb\u03c9\u03c1\u1f78\u03bd \u03b5\u1f30\u03c2 \u03b2\u03c1\u1ff6\u03c3\u03b9\u03bd. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "31",
            "french_version": "Et Dieu regarda toutes les choses qu'il avait cr\u00e9\u00e9es\u2009; et les trouva excellemment bonnes. Et il y eut un soir, et il y eut un matin, et ce fut un sixi\u00e8me jour.",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f70 \u03c0\u1f71\u03bd\u03c4\u03b1, \u1f45\u03c3\u03b1 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd, \u03ba\u03b1\u1f76 \u1f30\u03b4\u03bf\u1f7a \u03ba\u03b1\u03bb\u1f70 \u03bb\u1f77\u03b1\u03bd. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u1f11\u03c3\u03c0\u1f73\u03c1\u03b1 \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03c0\u03c1\u03c9\u1f77, \u1f21\u03bc\u1f73\u03c1\u03b1 \u1f15\u03ba\u03c4\u03b7."
        }
    ]
    data = [point.__dict__() for point in get_all_verses_for(SeptuagintBook.genese, 1)]
    assert data == expected_result


def test_get_all_verses_septuagint() -> None:
    for book in SeptuagintBook.__members__.values():

        nb_chapters = get_nb_chapters_for(book)
        for chapter_n in sorted(range(1, nb_chapters + 1)[::3]):

            debug_log.debug(f"Checking data integrity for {book}, chapter n° {chapter_n}")

            nb_verses = get_nb_verses_for(book, chapter_n)
            data = [point.__dict__() for point in get_all_verses_for(book, chapter_n)]

            assert len(data) == nb_verses

            for point in data:
                for _, v in point.items():
                    assert v is not None


def test_get_all_verses_ntgf() -> None:
    for book in NewTestamentBook.__members__.values():

        nb_chapters = get_nb_chapters_for(book)
        for chapter_n in sorted(range(1, nb_chapters + 1)[::3]):

            debug_log.debug(f"Checking data integrity for {book}, chapter n° {chapter_n}")

            nb_verses = get_nb_verses_for(book, chapter_n)
            data = [point.__dict__() for point in get_all_verses_for(book, chapter_n)]

            assert len(data) == nb_verses

            for point in data:
                for _, v in point.items():
                    assert v is not None


def test_get_verse_for() -> None:
    expected_result = [
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "1",
            "french_version": "Au commencement Dieu cr\u00e9a le ciel et la terre.",
            "greek_version": "\u1f18\u03bd \u1f00\u03c1\u03c7\u1fc7 \u1f10\u03c0\u03bf\u1f77\u03b7\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f78\u03bd \u03bf\u1f50\u03c1\u03b1\u03bd\u1f78\u03bd \u03ba\u03b1\u1f76 \u03c4\u1f74\u03bd \u03b3\u1fc6\u03bd."
        },
        {
            "book": "matthieu",
            "book_name": "Matthieu",
            "book_greek_name": "\u039a\u03b1\u03c4\u03b1 \u03bc\u03b1\u03b8\u03b8\u03b1\u03b9\u03bf\u03bd",
            "chapter_num": 1,
            "verse_num": "1",
            "french_version": "Livre de la g\u00e9n\u00e9alogie de J\u00e9sus-Christ, fils de David, fils d'Abraham.",
            "greek_version": "\u0392\u1f77\u03b2\u03bb\u03bf\u03c2 \u03b3\u03b5\u03bd\u1f73\u03c3\u03b5\u03c9\u03c2 \u1f38\u03b7\u03c3\u03bf\u1fe6 \u03a7\u03c1\u03b9\u03c3\u03c4\u03bf\u1fe6 \u03c5\u1f31\u03bf\u1fe6 \u0394\u03b1\u03c5\u1f76\u03b4 \u03c5\u1f31\u03bf\u1fe6 \u1f08\u03b2\u03c1\u03b1\u1f71\u03bc."
        },
        {
            "book": "josue",
            "book_name": "Josu\u00e9",
            "book_greek_name": "\u0399\u03b7\u03c3\u03bf\u03c5\u03c2",
            "chapter_num": 9,
            "verse_num": "2c",
            "french_version": "Et sur les pierres il \u00e9crivit le Deut\u00e9ronome, la loi de Mo\u00efse, devant les fils d'Isra\u00ebl. ",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f14\u03b3\u03c1\u03b1\u03c8\u03b5\u03bd \u1f38\u03b7\u03c3\u03bf\u1fe6\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1ff6\u03bd \u03bb\u1f77\u03b8\u03c9\u03bd \u03c4\u1f78 \u03b4\u03b5\u03c5\u03c4\u03b5\u03c1\u03bf\u03bd\u1f79\u03bc\u03b9\u03bf\u03bd, \u03bd\u1f79\u03bc\u03bf\u03bd \u039c\u03c9\u03c5\u03c3\u1fc6, \u1f43\u03bd \u1f14\u03b3\u03c1\u03b1\u03c8\u03b5\u03bd \u1f10\u03bd\u1f7d\u03c0\u03b9\u03bf\u03bd \u03c5\u1f31\u1ff6\u03bd \u0399\u03c3\u03c1\u03b1\u03b7\u03bb."
        }
    ]
    data = [
        get_verse_for(SeptuagintBook.genese, 1, "1").__dict__(),
        get_verse_for(NewTestamentBook.matthieu, 1, "1").__dict__(),
        get_verse_for(SeptuagintBook.josue, 9, "2c").__dict__(),
    ]
    assert data == expected_result


def test_get_verses_for() -> None:
    expected_result = [
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "9",
            "french_version": "Apr\u00e8s quoi Dieu dit\u2009: Que les eaux, au-dessous du ciel, soient r\u00e9unies en un seul amas, et que l'aride apparaisse. Et il en fut ainsi\u2009: les eaux, au-dessous du ciel, furent r\u00e9unies en un seul amas, et l'aride apparut.",
            "greek_version": "\u039a\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u03a3\u03c5\u03bd\u03b1\u03c7\u03b8\u1f75\u03c4\u03c9 \u03c4\u1f78 \u1f55\u03b4\u03c9\u03c1 \u03c4\u1f78 \u1f51\u03c0\u03bf\u03ba\u1f71\u03c4\u03c9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03b5\u1f30\u03c2 \u03c3\u03c5\u03bd\u03b1\u03b3\u03c9\u03b3\u1f74\u03bd \u03bc\u1f77\u03b1\u03bd, \u03ba\u03b1\u1f76 \u1f40\u03c6\u03b8\u1f75\u03c4\u03c9 \u1f21 \u03be\u03b7\u03c1\u1f71. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2. \u03ba\u03b1\u1f76 \u03c3\u03c5\u03bd\u1f75\u03c7\u03b8\u03b7 \u03c4\u1f78 \u1f55\u03b4\u03c9\u03c1 \u03c4\u1f78 \u1f51\u03c0\u03bf\u03ba\u1f71\u03c4\u03c9 \u03c4\u03bf\u1fe6 \u03bf\u1f50\u03c1\u03b1\u03bd\u03bf\u1fe6 \u03b5\u1f30\u03c2 \u03c4\u1f70\u03c2 \u03c3\u03c5\u03bd\u03b1\u03b3\u03c9\u03b3\u1f70\u03c2 \u03b1\u1f50\u03c4\u1ff6\u03bd, \u03ba\u03b1\u1f76 \u1f64\u03c6\u03b8\u03b7 \u1f21 \u03be\u03b7\u03c1\u1f71."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "10",
            "french_version": "Dieu appela l'aride terre\u2009; il appela mers l'amas des eaux. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u1f74\u03bd \u03be\u03b7\u03c1\u1f70\u03bd \u03b3\u1fc6\u03bd \u03ba\u03b1\u1f76 \u03c4\u1f70 \u03c3\u03c5\u03c3\u03c4\u1f75\u03bc\u03b1\u03c4\u03b1 \u03c4\u1ff6\u03bd \u1f51\u03b4\u1f71\u03c4\u03c9\u03bd \u1f10\u03ba\u1f71\u03bb\u03b5\u03c3\u03b5\u03bd \u03b8\u03b1\u03bb\u1f71\u03c3\u03c3\u03b1\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "11",
            "french_version": "Et Dieu dit\u2009: Que la terre produise des plantes herbac\u00e9es, portant semence selon les esp\u00e8ces et les similitudes, et des arbres fertiles en fruits, qui aient en eux les semences propres \u00e0 chaque esp\u00e8ce sur la terre. Et il en fut ainsi\u2009:",
            "greek_version": "\u03ba\u03b1\u1f76 \u03b5\u1f36\u03c0\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f79\u03c2 \u0392\u03bb\u03b1\u03c3\u03c4\u03b7\u03c3\u1f71\u03c4\u03c9 \u1f21 \u03b3\u1fc6 \u03b2\u03bf\u03c4\u1f71\u03bd\u03b7\u03bd \u03c7\u1f79\u03c1\u03c4\u03bf\u03c5, \u03c3\u03c0\u03b5\u1fd6\u03c1\u03bf\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03ba\u03b1\u03b8 \u1f41\u03bc\u03bf\u03b9\u1f79\u03c4\u03b7\u03c4\u03b1, \u03ba\u03b1\u1f76 \u03be\u1f7b\u03bb\u03bf\u03bd \u03ba\u1f71\u03c1\u03c0\u03b9\u03bc\u03bf\u03bd \u03c0\u03bf\u03b9\u03bf\u1fe6\u03bd \u03ba\u03b1\u03c1\u03c0\u1f79\u03bd, \u03bf\u1f57 \u03c4\u1f78 \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03b1\u1f50\u03c4\u03bf\u1fe6 \u1f10\u03bd \u03b1\u1f50\u03c4\u1ff7 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2. \u03ba\u03b1\u1f76 \u1f10\u03b3\u1f73\u03bd\u03b5\u03c4\u03bf \u03bf\u1f55\u03c4\u03c9\u03c2."
        },
        {
            "book": "genese",
            "book_name": "Gen\u00e8se",
            "book_greek_name": "\u0393\u03b5\u03bd\u03b5\u03c3\u03b9\u03c2",
            "chapter_num": 1,
            "verse_num": "12",
            "french_version": "La terre produisit des plantes herbac\u00e9es, portant semence selon les esp\u00e8ces et les similitudes, et des arbres fertiles en fruits ayant en eux les semences propres \u00e0 chaque esp\u00e8ce sur la terre. Et Dieu vit que cela \u00e9tait bien.",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f10\u03be\u1f75\u03bd\u03b5\u03b3\u03ba\u03b5\u03bd \u1f21 \u03b3\u1fc6 \u03b2\u03bf\u03c4\u1f71\u03bd\u03b7\u03bd \u03c7\u1f79\u03c1\u03c4\u03bf\u03c5, \u03c3\u03c0\u03b5\u1fd6\u03c1\u03bf\u03bd \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u03ba\u03b1\u1f76 \u03ba\u03b1\u03b8 \u1f41\u03bc\u03bf\u03b9\u1f79\u03c4\u03b7\u03c4\u03b1, \u03ba\u03b1\u1f76 \u03be\u1f7b\u03bb\u03bf\u03bd \u03ba\u1f71\u03c1\u03c0\u03b9\u03bc\u03bf\u03bd \u03c0\u03bf\u03b9\u03bf\u1fe6\u03bd \u03ba\u03b1\u03c1\u03c0\u1f79\u03bd, \u03bf\u1f57 \u03c4\u1f78 \u03c3\u03c0\u1f73\u03c1\u03bc\u03b1 \u03b1\u1f50\u03c4\u03bf\u1fe6 \u1f10\u03bd \u03b1\u1f50\u03c4\u1ff7 \u03ba\u03b1\u03c4\u1f70 \u03b3\u1f73\u03bd\u03bf\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1fc6\u03c2 \u03b3\u1fc6\u03c2. \u03ba\u03b1\u1f76 \u03b5\u1f36\u03b4\u03b5\u03bd \u1f41 \u03b8\u03b5\u1f78\u03c2 \u1f45\u03c4\u03b9 \u03ba\u03b1\u03bb\u1f79\u03bd."
        }
    ]
    data = [point.__dict__() for point in get_verses_for(SeptuagintBook.genese, 1, ["9", "12"])]
    assert data == expected_result

    expected_result = [
        {
            "book": "josue",
            "book_name": "Josu\u00e9",
            "book_greek_name": "\u0399\u03b7\u03c3\u03bf\u03c5\u03c2",
            "chapter_num": 9,
            "verse_num": "2",
            "french_version": "Ils se r\u00e9unirent \u00e0 la fois pour combattre Josu\u00e9 et Isra\u00ebl. ",
            "greek_version": "\u03c3\u03c5\u03bd\u1f75\u03bb\u03b8\u03bf\u03c3\u03b1\u03bd \u1f10\u03c0\u1f76 \u03c4\u1f78 \u03b1\u1f50\u03c4\u1f78 \u1f10\u03ba\u03c0\u03bf\u03bb\u03b5\u03bc\u1fc6\u03c3\u03b1\u03b9 \u1f38\u03b7\u03c3\u03bf\u1fe6\u03bd \u03ba\u03b1\u1f76 \u0399\u03c3\u03c1\u03b1\u03b7\u03bb \u1f05\u03bc\u03b1 \u03c0\u1f71\u03bd\u03c4\u03b5\u03c2."
        },
        {
            "book": "josue",
            "book_name": "Josu\u00e9",
            "book_greek_name": "\u0399\u03b7\u03c3\u03bf\u03c5\u03c2",
            "chapter_num": 9,
            "verse_num": "2a",
            "french_version": "Alors, Josu\u00e9 \u00e9leva un autel au Seigneur Dieu d'Isra\u00ebl sur le mont Hebal, ",
            "greek_version": "\u03a4\u1f79\u03c4\u03b5 \u1fa0\u03ba\u03bf\u03b4\u1f79\u03bc\u03b7\u03c3\u03b5\u03bd \u1f38\u03b7\u03c3\u03bf\u1fe6\u03c2 \u03b8\u03c5\u03c3\u03b9\u03b1\u03c3\u03c4\u1f75\u03c1\u03b9\u03bf\u03bd \u03ba\u03c5\u03c1\u1f77\u1ff3 \u03c4\u1ff7 \u03b8\u03b5\u1ff7 \u0399\u03c3\u03c1\u03b1\u03b7\u03bb \u1f10\u03bd \u1f44\u03c1\u03b5\u03b9 \u0393\u03b1\u03b9\u03b2\u03b1\u03bb,"
        },
        {
            "book": "josue",
            "book_name": "Josu\u00e9",
            "book_greek_name": "\u0399\u03b7\u03c3\u03bf\u03c5\u03c2",
            "chapter_num": 9,
            "verse_num": "2b",
            "french_version": "Selon ce que Mo\u00efse, serviteur de Dieu, avait prescrit aux fils d'Isra\u00ebl et qu'il est \u00e9crit en la loi de Mo\u00efse\u2009; cet autel fut construit en pierres brutes que le fer n'avait point travaill\u00e9es\u2009; Josu\u00e9 y posa des holocaustes au Seigneur et des sacrifices de d\u00e9livrance. ",
            "greek_version": "\u03ba\u03b1\u03b8\u1f79\u03c4\u03b9 \u1f10\u03bd\u03b5\u03c4\u03b5\u1f77\u03bb\u03b1\u03c4\u03bf \u039c\u03c9\u03c5\u03c3\u1fc6\u03c2 \u1f41 \u03b8\u03b5\u03c1\u1f71\u03c0\u03c9\u03bd \u03ba\u03c5\u03c1\u1f77\u03bf\u03c5 \u03c4\u03bf\u1fd6\u03c2 \u03c5\u1f31\u03bf\u1fd6\u03c2 \u0399\u03c3\u03c1\u03b1\u03b7\u03bb, \u03ba\u03b1\u03b8\u1f70 \u03b3\u1f73\u03b3\u03c1\u03b1\u03c0\u03c4\u03b1\u03b9 \u1f10\u03bd \u03c4\u1ff7 \u03bd\u1f79\u03bc\u1ff3 \u039c\u03c9\u03c5\u03c3\u1fc6, \u03b8\u03c5\u03c3\u03b9\u03b1\u03c3\u03c4\u1f75\u03c1\u03b9\u03bf\u03bd \u03bb\u1f77\u03b8\u03c9\u03bd \u1f41\u03bb\u03bf\u03ba\u03bb\u1f75\u03c1\u03c9\u03bd, \u1f10\u03c6 \u03bf\u1f53\u03c2 \u03bf\u1f50\u03ba \u1f10\u03c0\u03b5\u03b2\u03bb\u1f75\u03b8\u03b7 \u03c3\u1f77\u03b4\u03b7\u03c1\u03bf\u03c2, \u03ba\u03b1\u1f76 \u1f00\u03bd\u03b5\u03b2\u1f77\u03b2\u03b1\u03c3\u03b5\u03bd \u1f10\u03ba\u03b5\u1fd6 \u1f41\u03bb\u03bf\u03ba\u03b1\u03c5\u03c4\u1f7d\u03bc\u03b1\u03c4\u03b1 \u03ba\u03c5\u03c1\u1f77\u1ff3 \u03ba\u03b1\u1f76 \u03b8\u03c5\u03c3\u1f77\u03b1\u03bd \u03c3\u03c9\u03c4\u03b7\u03c1\u1f77\u03bf\u03c5."
        },
        {
            "book": "josue",
            "book_name": "Josu\u00e9",
            "book_greek_name": "\u0399\u03b7\u03c3\u03bf\u03c5\u03c2",
            "chapter_num": 9,
            "verse_num": "2c",
            "french_version": "Et sur les pierres il \u00e9crivit le Deut\u00e9ronome, la loi de Mo\u00efse, devant les fils d'Isra\u00ebl. ",
            "greek_version": "\u03ba\u03b1\u1f76 \u1f14\u03b3\u03c1\u03b1\u03c8\u03b5\u03bd \u1f38\u03b7\u03c3\u03bf\u1fe6\u03c2 \u1f10\u03c0\u1f76 \u03c4\u1ff6\u03bd \u03bb\u1f77\u03b8\u03c9\u03bd \u03c4\u1f78 \u03b4\u03b5\u03c5\u03c4\u03b5\u03c1\u03bf\u03bd\u1f79\u03bc\u03b9\u03bf\u03bd, \u03bd\u1f79\u03bc\u03bf\u03bd \u039c\u03c9\u03c5\u03c3\u1fc6, \u1f43\u03bd \u1f14\u03b3\u03c1\u03b1\u03c8\u03b5\u03bd \u1f10\u03bd\u1f7d\u03c0\u03b9\u03bf\u03bd \u03c5\u1f31\u1ff6\u03bd \u0399\u03c3\u03c1\u03b1\u03b7\u03bb."
        }
    ]
    data = [point.__dict__() for point in get_verses_for(SeptuagintBook.josue, 9, ["2", "2c"])]
    assert data == expected_result


def test_get_book_greek_name() -> None:
    expected_result = ["Γενεσις", "Κατα μαθθαιον"]
    genesis_html = _get_markup_for(SeptuagintBook.genese, 1)
    matthew_html = _get_markup_for(NewTestamentBook.matthieu, 1)
    data = [_get_book_greek_name(genesis_html), _get_book_greek_name(matthew_html)]
    assert data == expected_result
