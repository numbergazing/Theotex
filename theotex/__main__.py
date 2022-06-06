#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
from typing import List

from theotex import _slugify, _get_book, CorpusName, SeptuagintBookName, NewTestamentBookName
from theotex.navigation import get_verse_for, get_verses_for


def _init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog="theotex",
        usage="theotex.py [OPTIONS]",
        description="Print Bible verses in French and Greek from https://theotex.org."
    )
    parser.add_argument("-v", "--version", action="version", version=f"theotex version 1.0.0")
    parser.add_argument(
        "--get-verses",
        action="store",
        nargs=3,
        metavar="",
        help="display verses (usage examples: Jean 3 16, Proverbes 3 5:6)"
    )
    parser.add_argument(
        "--only-french",
        action="store_true",
        default=False,
        help="display the verses in french only."
    )
    parser.add_argument(
        "--only-greek",
        action="store_true",
        default=False,
        help="display the verses in greek only."
    )
    parser.add_argument(
        "--get-corpora",
        action="store_true",
        default=False,
        help="display a list of the available corpora."
    )
    parser.add_argument(
        "--get-books",
        action="store",
        nargs=1,
        metavar="CORPUS",
        help="display a list of the available books for a corpus."
    )

    return parser


def _get_corpora() -> str:

    corpora: List[str]
    message: str

    corpora = [member.value for member in CorpusName.__members__.values()]
    message = "\n".join(corpora)
    print(message)

    return message


def _get_books(args: argparse.Namespace) -> str:

    slugified_corpus: str
    corpora: List[str]
    books: List[str]

    slugified_corpus = _slugify(args.get_books[0])
    corpora = [_slugify(member.value) for member in CorpusName.__members__.values()]

    if slugified_corpus not in corpora:
        sys.exit(f"The corpus {args.get_books[0]} does not exist.")

    match slugified_corpus:
        case "septante":
            books = [member.value for member in SeptuagintBookName.__members__.values()]
        case "nouveau_testament":
            books = [member.value for member in NewTestamentBookName.__members__.values()]

    message = "\n".join(books)
    print(message)

    return message


def _get_verses(args: argparse.Namespace) -> str:

    message: str
    book_slug: str
    verse_refs: List[str]
    filtered_refs: set

    message = str()
    book_slug = _slugify(args.get_verses[0])
    verse_refs = args.get_verses[2].split(":")
    filtered_refs = set(verse_refs) - {""}
    verse_refs = list(filtered_refs)

    if args.only_french is True and args.only_greek is True:
        sys.exit("You can only use one of these options (--only-french, --only-greek) at a time.")

    if len(verse_refs) > 1:

        to_erase_index: int

        if args.only_french:
            to_erase_index = -1
        elif args.only_greek:
            to_erase_index = -1
        else:
            to_erase_index = -2

        for verse in get_verses_for(_get_book(book_slug), int(args.get_verses[1]), verse_refs):
            if args.only_french:
                message += f"{verse.get_french_str}\n"
            elif args.only_greek:
                message += f"{verse.get_greek_str}\n"
            else:
                message += f"{str(verse)}\n\n"

        message = message[:to_erase_index]

    else:
        verse = get_verse_for(_get_book(book_slug), int(args.get_verses[1]), verse_refs[0])
        if args.only_french:
            message = verse.get_french_str
        elif args.only_greek:
            message = verse.get_greek_str
        else:
            message = str(verse)

    print(f"{message}")
    return message


def main():

    parser: argparse.ArgumentParser
    args: argparse.Namespace

    parser = _init_argparse()
    args = parser.parse_args()

    if args.get_corpora is True:
        return _get_corpora()

    if args.get_books is not None:
        return _get_books(args)

    if args.get_verses is not None:
        return _get_verses(args)


main()
sys.exit(0)
