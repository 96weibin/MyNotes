import argparse
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
import sys

from test import get_adult_names, openfile, parse_lines


log_dir = Path(__file__).parent / "logs"
log_dir.mkdir(exist_ok=True)

file_handler = TimedRotatingFileHandler(
    filename=log_dir / "task.log",
    when="midnight",      # 每天切分
    interval=1,
    backupCount=14,       # 保留 14 天
    encoding="utf-8"
)

stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[stream_handler, file_handler],
)

def main() -> int:
    parser = argparse.ArgumentParser(description="file name, and min age")
    parser.add_argument("--file", required=True, help="The file name to process")
    parser.add_argument("--min_age", type=int, default=18, help="The minimum age to filter")
    parser.add_argument("--verbose", action="store_true", help="Print debug info")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        logging.error(f"file not found: {file_path}")
        return 2

    lines = openfile(file_path)
    users = parse_lines(lines)
    adult_names = get_adult_names(users, args.min_age)

    if args.verbose:
        logging.info(f"total lines: {len(lines)}")
        logging.info(f"parsed users: {len(users)}")
        logging.info(f"min_age: {args.min_age}")

    print(adult_names)
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as e:
        print(f"[ERROR] unexpected: {type(e).__name__}: {e}")
        code = 1
    raise SystemExit(code)