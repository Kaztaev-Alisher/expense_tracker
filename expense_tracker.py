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

def total_by(expenses : list[Expense], by_month: bool) -> dict[str , float]:
    totals : dict[str , float] = {}
    for expense in expenses:
        group = expense[1]
        if by_month:
            group = expense[0][:7]
        totals[group] = totals.get(group , 0) + expense[2]
    return totals

def format_totals(title: str , totals : dict[str , float]) -> list[str]:
    ordered = sorted(totals.items(), key=lambda pair: pair[0])
    return [title] + [f"{name}: {amount:.2f}" for name, amount in ordered]


def parse_args(argv: list[str]) -> str | None:
    if len(argv) != 1:
        return None
    return argv[0]

def main() -> int:
    path = parse_args(sys.argv[1:])
    if path is None:
        print("Использование: python expense_tracker.py <файл.csv>", file=sys.stderr)
        return 1

    expenses = read_expenses(path)
    by_category = total_by(expenses , False)
    by_month = total_by(expenses , True)
    
    print("\n".join(format_totals("По категориям:", by_category)))
    print()
    print("\n".join(format_totals("По месяцам:", by_month)))
    return 0

if __name__ == "__main__":
    sys.exit(main())