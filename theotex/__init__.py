from dataclasses import dataclass
from enum import Enum
from typing import Union


class TheotexEnum(Enum):

    def __repr__(self):
        return self.value


class Corpus(TheotexEnum):
    SEPTUAGINT = "septuaginta"
    NEW_TESTAMENT = "ntgf"


class SeptuagintBook(TheotexEnum):
    GENESIS = "genese"
    EXODUS = "exode"
    LEVITICUS = "levitique"
    NUMBERS = "nombres"
    DEUTERONOMY = "deuteronome"
    JOSHUA = "josue"
    JUDGES = "juges"
    RUTH = "ruth"
    KINGS1 = "1rois"
    KINGS2 = "2rois"
    KINGS3 = "3rois"
    KINGS4 = "4rois"
    CHRONICLES1 = "1chroniques"
    CHRONICLES2 = "2chroniques"
    EZRA1 = "1esdras"
    EZRA2 = "2esdras"
    ESTHER = "esther"
    JUDITH = "judith"
    TOBIT = "tobie"
    MACCABEES1 = "1maccabees"
    MACCABEES2 = "2maccabees"
    MACCABEES3 = "3maccabees"
    MACCABEES4 = "4maccabees"
    PSALMS = "psaumes"
    PROVERBS = "proverbes"
    ECCLESIASTES = "ecclesiastes"
    SONG_OF_SOLOMON = "cantique"
    JOB = "job"
    WISDOM = "sagesse"
    SIRACID = "siracide"
    PSALMS_OF_SOLOMON = "salomon_psaumes"
    HOSEA = "osee"
    AMOS = "amos"
    MICAH = "michee"
    JOEL = "joel"
    OBADIAH = "abdias"
    JONAH = "jonas"
    NAHUM = "nahum"
    HABAKKUK = "habakuk"
    ZEPHANIAH = "sophonie"
    HAGGAI = "aggee"
    ZECHARIAH = "zacharie"
    MALACHI = "malachie"
    ISAIAH = "esaie"
    JEREMIAH = "jeremie"
    BARUCH = "baruch"
    LAMENTATIONS = "lamentations"
    EPISTLE_OF_JEREMIAH = "lettre_jeremie"
    EZEKIEL = "ezechiel"
    SUSANNA = "suzanne_theod"
    DANIEL = "daniel_theod"
    BEL = "bel_theod"


class NewTestamentBook(TheotexEnum):
    MATTHEW = "matthieu"
    MARK = "marc"
    LUKE = "luc"
    JOHN = "jean"
    ACTS = "actes"
    ROMANS = "romains"
    CORINTHIANS1 = "1corinthiens"
    CORINTHIANS2 = "2corinthiens"
    GALATIANS = "galates"
    EPHESIANS = "ephesiens"
    PHILIPPIANS = "philippiens"
    COLOSSIANS = "colossiens"
    THESSALONIANS1 = "1thessaloniciens"
    THESSALONIANS2 = "2thessaloniciens"
    TIMOTHY1 = "1timothee"
    TIMOTHY2 = "2timothee"
    TITUS = "tite"
    PHILEMON = "philemon"
    HEBREWS = "hebreux"
    JAMES = "jacques"
    PETER1 = "1pierre"
    PETER2 = "2pierre"
    JOHN1 = "1jean"
    JOHN2 = "2jean"
    JOHN3 = "3jean"
    JUDE = "jude"
    REVELATION = "apocalypse"


Book = Union[SeptuagintBook, NewTestamentBook]


@dataclass
class Verse:

    book: Book
    chapter_num: int
    verse_num: str  # verse num is a string because some verses are referenced with a number and a letter like : "2c"
    french_version: str
    greek_version: str

    def __dict__(self):
        return {
            "book": self.book.value,
            "chapter_num": self.chapter_num,
            "verse_num": self.verse_num,
            "french_version": self.french_version,
            "greek_version": self.greek_version,
        }
