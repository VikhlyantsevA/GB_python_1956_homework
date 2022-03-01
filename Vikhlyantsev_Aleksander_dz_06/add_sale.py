# Задание 6

import argparse
import re
import sys


def add_sale(sale: str, mode: str):
    """
    Writing sales value to bakery.csv.
    :sale: sales value
    """
    with open('bakery.csv', mode) as f:
        f.write(f'{sale}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing sales value.')
    parser.add_argument('-m',
                        type=str,
                        default='a',
                        choices=['a', 'w'],
                        help='Writing mode: a - append to bakery.csv (default); w - rewrite to bakery.csv.')

    parser.add_argument('sale',
                        type=str,
                        help='Total sales.')

    args = parser.parse_args()
    mode = args.m
    sale = args.sale.replace('.', ',')

    # Добавил доппроверку с решуляркой. Знаю что на момент урока мы не проходили этого.
    if not re.match(r'\d+,?\d*', sale):
        raise TypeError(f'Sale is not decimal-like type.')

    sys.exit(add_sale(sale, mode))
