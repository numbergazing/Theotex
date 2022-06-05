#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from theotex import _slugify, SeptuagintBook
from theotex.navigation import get_verse_for, get_verses_for


def _init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        usage="theotex.py [OPTION] [BOOK] [CHAPTER] [VERSE]",
        description="Print Bible verses in French and Greek from https://theotex.org."
    )
    parser.add_argument("-v", "--version", action="version", version=f"theotex version 1.0.0")
    parser.add_argument(
        "--get-verses",
        action="store",
        nargs=3,
        metavar="",
        help="display verses referenced with [book] [chapter] [verse] or [verse:verse]"
    )

    return parser


def main():

    parser: argparse.ArgumentParser
    args: argparse.Namespace
    message: str

    message = str()
    parser = _init_argparse()
    args = parser.parse_args()

    if args.get_verses is not None:

        book_slug = _slugify(args.get_verses[0])
        verse_refs = args.get_verses[2].split(":")

        if len(verse_refs) > 1:
            for verse in get_verses_for(SeptuagintBook[book_slug], int(args.get_verses[1]), verse_refs):
                message += f"{str(verse)}\n\n"
            message = message[:-2]
        else:
            verse = get_verse_for(SeptuagintBook[book_slug], int(args.get_verses[1]), verse_refs[0])
            message = str(verse)

    print(f"{message}")
    return message


main()
