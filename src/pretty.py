#!/bin/env python3

"""
Programa que le da formato (pretty print) a ficheros json y xml.
AUTHOR = Gabriel Reus Rodriguez
"""

import argparse
import xml.dom.minidom
import os
import json
import sys

PROG_NAME = "pretty"
PROG_DESCRIPTION = """Programa que formatea ficheros xml o json."""


# Auxiliar classes
class ArgException(Exception):
    pass


# Functions
def treat_args():
    parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESCRIPTION)

    parser.add_argument("-x", "--xml", type=str, required=False, help="XML file")
    parser.add_argument("-j", "--json", type=str, required=False, help="JSON file")
    parser.add_argument(
        "-a", "--auto", type=str, required=False, help="Autodetect file"
    )
    parser.add_argument("-o", "--output", type=str, required=True, help="Output file")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose")

    args = parser.parse_args()
    return parser, args


def format_xml(args: argparse.Namespace):
    dom = None
    try:
        dom = xml.dom.minidom.parse(args.xml)
    except Exception as e:
        print(f"\tError al leer el fichero {args.xml}: {e}")
        sys.exit(1)
    pretty_formated = dom.toprettyxml()
    try:
        with open(file=args.output, mode="w") as f:
            f.write(pretty_formated)
    except Exception as e:
        print(f"\tError al escribir el fichero {args.output}: {e}")
        sys.exit(1)


def format_json(args: argparse.Namespace):
    data = None
    if args.verbose:
        print(f"Voy a leer: {args.json}")
    try:
        with open(file=args.json, mode="r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"\tError al leer el fichero {args.json} err: {e}")
        sys.exit(1)
    try:
        with open(file=args.output, mode="w") as f:
            json.dump(data, fp=f, sort_keys=True, indent=4)
    except Exception as e:
        print(f"\tError al escribir el fichero {args.output}: {e}")
        sys.exit(1)


def format_auto(args: argparse.Namespace):
    filename, file_extension = os.path.splitext(args.auto)
    if file_extension.lower() == ".xml":
        args.xml = args.auto
        format_xml(args)
        return
    if file_extension.lower() == ".json":
        args.json = args.auto
        format_json(args)
        return
    print(f"ERROR: extension NO identificada {args.auto}")
    sys.exit(1)


def pretty(args: argparse.Namespace):
    if args.xml is not None:
        format_xml(args)
        return
    if args.json is not None:
        format_json(args)
        return
    if args.auto is not None:
        format_auto(args)
        return
    raise ArgException()


# main
if __name__ == "__main__":
    parser, args = treat_args()
    try:
        pretty(args)
    except ArgException:
        print("\tError parseando los argumentos")
        parser.print_help()
