# Задание 6

import argparse
import sys


def show_sales(start_line: int, end_line: int):
    """
    Reading sales values from bakery.csv.
    @param start_line: Line to start reading from
    @param end_line: Line to stop reading at
    """
    with open('bakery.csv') as f:
        if not start_line:
            print(*f.readlines(), sep='')
        else:
            for i, line in enumerate(f, start=1):
                if i >= start_line:
                    if end_line:
                        if i > end_line:
                            break
                    print(line.strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reading sales value.')
    parser.add_argument('start_line',
                        type=int,
                        nargs='?',
                        help='Line to start reading from.')

    parser.add_argument('end_line',
                        type=int,
                        nargs='?',
                        help='Line to stop reading at.')

    args = parser.parse_args()
    start_line = args.start_line
    end_line = args.end_line

    sys.exit(show_sales(start_line, end_line))
