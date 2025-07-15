import csv
import sys
import math
from collections import defaultdict, Counter

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def analyze_column(values):
    numeric = [float(v) for v in values if is_number(v)]
    stats = {}
    stats["count"] = len(values)
    if numeric:
        stats["mean"] = sum(numeric) / len(numeric)
        stats["min"] = min(numeric)
        stats["max"] = max(numeric)
        stats["std_dev"] = (sum((x - stats["mean"])**2 for x in numeric) / len(numeric))**0.5
    else:
        freq = Counter(values)
        stats["unique_count"] = len(freq)
        stats["most_common"] = freq.most_common(1)[0] if freq else None
    return stats

def load_csv(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        columns = defaultdict(list)
        for row in reader:
            for key, value in row.items():
                columns[key].append(value.strip())
        return columns

def main():
    if len(sys.argv) != 2:
        print("Usage: python pure_python_stats.py <csv_file>")
        sys.exit(1)

    filename = sys.argv[1]
    columns = load_csv(filename)

    print(f"\n📊 Descriptive Statistics for {filename}\n")
    for col, values in columns.items():
        print(f"Column: {col}")
        stats = analyze_column(values)
        for k, v in stats.items():
            print(f"  {k}: {v}")
        print()

if __name__ == "__main__":
    main()
