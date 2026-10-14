import sys
from tablestats import read_rows, count_types, total_minutes, to_csv
def main():
    try:
        path = imput().strip()
    except EOFError:
        return
    with open(path, encoding="utf-8") as table:
        rows = read_rows(table)
    total_records = len(rows)
    counts = count_types(rows)
    unique_types = len(counts)
    error_minutes = total_minutes(rows, "ошибка")
    print(total_records)
    print(unique_types)
    print(error_minutes)
    summary_content = to_csv(counts)

    with open("summary.csv", "w", encoding="utf-8") as out:
     out.write(to_csv(counts))
