from pathlib import Path

def openfile(filePath: Path) -> list[str]:
    with open(filePath, 'r', encoding="utf-8") as file:
        return file.readlines();

def parse_line(line: str) -> dict[str, str | None]:
    parts= line.strip().split(',')

    return {
        'name': parts[0].strip() if len(parts) > 0 else None,
        'age': parts[1].strip() if len(parts) > 1 else None,
    }

def parse_lines(lines: list[str]) -> list[dict[str, str | None]]:
    return [parse_line(line) for line in lines if line.strip() != '']

def get_adult_names(users: list[dict[str, str | None]], min_age: int = 18) -> list[str]:
    def parese_age(age_str: str | None) -> int | None:
        try:
            return int(age_str)
        except (ValueError, TypeError):
            return None
    
    return [user["name"] for user in users if parese_age(user["age"]) and parese_age(user["age"]) >= min_age]

def main():
    dirpath = Path(__file__).parent
    lines = openfile(dirpath / '01.txt')
    parsed_users = parse_lines(lines)
    print(parsed_users)
    print(get_adult_names(parsed_users))

if __name__ == "__main__":
    try:
        main();
    except Exception as e:
        print(f"An error occurred: {e}")