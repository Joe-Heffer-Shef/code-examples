import argparse
import datetime

USAGE = """
To view help for this script:
python argument_parser.py --help
"""

def get_args():
    parser = argparse.ArgumentParser()

    # Automatically parse the user's input text into the appropriate data type
    parser.add_argument('-d', '--date', help='ISO date YYYY-MM-DD', type=datetime.date.fromisoformat)
    # Set the argument as mandatory
    parser.add_argument('-n', '--number', type=int, required=True)

    return parser.parse_args()


def main():
    args = get_args()
    logging.basicConfig(level=logging.DEBUG)

    print(repr(args.date))
    print(args.date)
    print(args.number)


if __name__ == '__main__':
    main()
