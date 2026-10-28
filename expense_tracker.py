import sys

def parse_args(argv: list[str]) -> str | None:
    if len(argv) != 1:
        return None
    return argv[0]

def main() -> int:
    path = parse_args(sys.argv[1:])
    if path is None:
        print("Использование: python expense_tracker.py <файл.csv>", file=sys.stderr)
        return 1
        
    print(f"Буду читать файл: {path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())