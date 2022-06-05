#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

from theotex import _slugify, _get_book
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
    parser.add_argument("--only-french", action="store_true", default=False, required=False)
    parser.add_argument("--only-greek", action="store_true", default=False, required=False)

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


main()
sys.exit(0)
