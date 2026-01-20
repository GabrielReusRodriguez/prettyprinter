#!/bin/env python3

"""
    Programa que le da formato (pretty print ) a ficheros  json y xml.
    AUTHOR = Gabriel Reus Rodriguez
"""

import argparse


PROG_NAME= 'pretty'
PROG_DESCRIPTION = """Programa que formatea ficheros xml o json.
"""

"""Auxiliar classes"""
class ArgException(Exception):
    pass

"""Functions"""
def treat_args():
    # Obtengo la instancia de argumentparser.
    parser = argparse.ArgumentParser(   prog= PROG_NAME,
                                        description= PROG_DESCRIPTION
                                    )

    parser.add_argument('-x', '--xml', nargs=1, type = str, help =' XML file')
    parser.add_argument('-j', '--json', nargs=1, type = str, help ='JSON file')
    # Para argumentos que no tienen valor, uso un action.store_true
    parser.add_argument('-a', '--auto', action= 'store_true', help ='Autodetect file')
    parser.add_argument('-v', '--verbose', action= 'store_true', help ='verbose')
    
    args = parser.parse_args()
    return (parser, args)


def format_xml(args:argparse.Namespace):
    pass

def format_json(args:argparse.Namespace):
    pass

def format_auto(args:argparse.Namespace):
    pass

def pretty(args: argparse.Namespace):
    if args.xml is not None:
        format_xml(args)
        return
    if args.json is not None:
        format_json(args)
        return
    if args.auto == True:
        format_auto(args)
        return
    raise ArgException()

"""main"""
if __name__ == '__main__':
    parser, args = treat_args()
    try:
        pretty(args)
    except ArgException as e:
        print(f'\tError parseando los argumentos')
        parser.print_help()
