import sys
import csv 
from datetime import date 

Expense = tuple[str , str , float]
REQUIRED_COLOUMNS = {"date" , "category" , "amount"}

def parse_row(row : dict[str , str]) -> Expense:
    raw_date = row.get("date")
    category = row.get("category")
    amount = float(row.get("amount"))
    return (raw_date, category, amount)

def read_expenses(path : str) -> list[Expense]:
    expenses: list[Expense] = []
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for line_no , row in enumerate(reader , start = 2):
            expenses.append(parse_row(row))
    return expenses

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
    expenses = read_expenses(path)
    print(f"Прочитано записей : {len(expenses)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())