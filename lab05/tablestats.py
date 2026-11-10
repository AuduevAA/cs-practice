def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = [part.strip() for part in line.split(',')]

        if header is None:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        rows.append(dict(zip(header, parts)))

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind is not None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get("тип") == kind:
            val = row.get("минуты", "")
            try:
                total += float(val.replace(',', '.'))
            except ValueError:
                continue

    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество\n"]

    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}\n")

    return "".join(lines)