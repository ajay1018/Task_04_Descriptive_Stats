import sys
import polars as pl

def main():
    if len(sys.argv) != 2:
        print("Usage: python polars_stats.py <csv_file>")
        sys.exit(1)

    filename = sys.argv[1]
    df = pl.read_csv(filename)

    print(f"\n📊 Descriptive Statistics for {filename}\n")
    print(df.describe())

    for col in df.columns:
        print(f"\nColumn: {col}")
        print("Unique values:", df[col].n_unique())
        print("Most frequent value:\n", df[col].value_counts().limit(1))

    group_keys = []
    if "page_id" in df.columns:
        group_keys.append("page_id")
    if "ad_id" in df.columns:
        group_keys.append("ad_id")

    if group_keys:
        print(f"\n📚 Grouped Statistics by {group_keys}")
        print(df.groupby(group_keys).agg(pl.count()))

if __name__ == "__main__":
    main()