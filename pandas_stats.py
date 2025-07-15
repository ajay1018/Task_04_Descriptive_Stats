import sys
import pandas as pd

def main():
    if len(sys.argv) != 2:
        print("Usage: python pandas_stats.py <csv_file>")
        sys.exit(1)

    filename = sys.argv[1]
    df = pd.read_csv(filename)

    print(f"\n📊 Descriptive Statistics for {filename}\n")
    print(df.describe(include='all'))

    for col in df.columns:
        print(f"\nColumn: {col}")
        print("Unique values:", df[col].nunique())
        print("Most frequent value:\n", df[col].value_counts().head(1))

    group_keys = []
    if "page_id" in df.columns:
        group_keys.append("page_id")
    if "ad_id" in df.columns:
        group_keys.append("ad_id")

    if group_keys:
        print(f"\n📚 Grouped Statistics by {group_keys}")
        grouped = df.groupby(group_keys)
        print(grouped.describe())

if __name__ == "__main__":
    main()