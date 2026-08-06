import argparse
from test import get_adult_names, openfile, parse_lines

def main():
    print("in test.py, __name__ =", __name__)
    parser = argparse.ArgumentParser(description="file name, and min age")
    parser.add_argument("--file", required=True, help="The file name to process")
    parser.add_argument("--min_age", type=int, help="The minimum age to filter")
    args = parser.parse_args()

    lines = openfile(args.file)
    users = parse_lines(lines)
    adult_names = get_adult_names(users, args.min_age)
    print(adult_names)
    # Add your main logic here


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")