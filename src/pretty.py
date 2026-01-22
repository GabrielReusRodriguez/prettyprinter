#!/bin/env python3

"""
    Programa que le da formato (pretty print ) a ficheros  json y xml.
    AUTHOR = Gabriel Reus Rodriguez
"""

import argparse
import xml.dom.minidom
import os
import json

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

    parser.add_argument('-x', '--xml', nargs=1, type = str, required= False, help =' XML file')
    parser.add_argument('-j', '--json', nargs=1, type = str, required= False, help ='JSON file')
    # Para argumentos que no tienen valor, uso un action.store_true
    #parser.add_argument('-a', '--auto', action= 'store_true', help ='Autodetect file')
    parser.add_argument('-a', '--auto', nargs=1, type = str, required= False, help ='Autodetect file' )
    parser.add_argument('-o', '--output', nargs=1, type = str, required= True, help ='Output file')
    parser.add_argument('-v', '--verbose', action= 'store_true', help ='verbose')
    
    args = parser.parse_args()
    return (parser, args)


def format_xml(args:argparse.Namespace):
    # Creo la instancia del dom.
    dom = None
    # La parseo
    try:
        dom = xml.dom.minidom.parse(args.xml[0])
    except Exception as e: 
        print(f'\tError al leer el fichero {args.xml[0]}: {e}')
        return
    # Hago el pretty printer
    pretty_formated = dom.toprettyxml()
    # Escribo los resultados.
    try:
        with open(file = args.output[0], mode= 'w') as f:
            f.write(pretty_formated)
    except IOError as e:
        print(f'\tError al escribir el fichero {args.output[0]}: {e}')
        return
    except:
        print(f'\tError al escribir el fichero {args.output[0]}')
        return


def format_json(args:argparse.Namespace):
    data = None
    # Leo el fichero
    print(f'Voy a leer: {args.json[0]}')
    try:
        with open(file = args.json[0], mode = 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f'\tError al leer el fichero {args.json[0]} err: {e}')
        return
    # Le doy formato y escribo el fichero
    try:
        with open(file = args.output[0], mode = 'w') as f:
            json.dump(data, fp = f, sort_keys = True, indent = 4)
    except IOError as e:
        print(f'\tError al escribir el fichero {args.json[0]}: {e}')
        return


def format_auto(args:argparse.Namespace):
    # Primero obtengo la extension del fichero.
    filename, file_extension = os.path.splitext(args.auto[0])
    if file_extension.lower() == '.xml':
        args.xml = [args.auto[0]]
        format_xml(args)
        return
    if file_extension.lower() == '.json':
        args.json = [args.auto[0]]
        format_json(args)
        return
    print(f'ERROR: extension NO identificada {args.auto[0]}')
    return

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

"""main"""
if __name__ == '__main__':
    parser, args = treat_args()
    try:
        pretty(args)
    except ArgException as e:
        print(f'\tError parseando los argumentos')
        parser.print_help()

