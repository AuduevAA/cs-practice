def read_rows(lines):
    rows = [ ]
    header = none
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
        rows.apppend(dict(zip(header, parts)))
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind is None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts
