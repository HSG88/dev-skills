import argparse
import json
from pathlib import Path
import sys

from exporter import render_orders


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('--columns', nargs='+', required=True)
    parser.add_argument('--status')
    parser.add_argument('--descending', action='store_true')
    args = parser.parse_args()
    orders = json.loads(args.input.read_text(encoding='utf-8'))
    sys.stdout.write(render_orders(orders, args.columns, args.status, args.descending))


if __name__ == '__main__':
    main()
