import pandas as pd


def load_working_hours(filepath):
    """Load and clean the annual working hours dataset."""
    df = pd.read_csv(filepath)

    df = df.rename(
        columns={
            "Entity": "country",
            "Year": "year",
            "Working hours per worker": "annual_working_hours",
        }
    )

    return df[["country", "year", "annual_working_hours"]]


def load_productivity(filepath):
    """Load and clean the labour productivity dataset."""
    df = pd.read_csv(filepath)

    df = df.rename(
        columns={
            "Entity": "country",
            "Year": "year",
            "Productivity: output per hour worked": "productivity_per_hour",
        }
    )

    return df[["country", "year", "productivity_per_hour"]]


def merge_datasets(hours_df, productivity_df):
    """Merge working hours and productivity observations by country and year."""
    merged_df = pd.merge(
        hours_df,
        productivity_df,
        on=["country", "year"],
        how="inner",
    )

    return merged_df.dropna().reset_index(drop=True)


def main():
    hours = load_working_hours("data/annual-working-hours-per-worker.csv")
    productivity = load_productivity("data/labour-productivity.csv")

    merged = merge_datasets(hours, productivity)

    print("Working hours data:")
    print(hours.head())

    print("\nProductivity data:")
    print(productivity.head())

    print("\nMerged data:")
    print(merged.head())

    print(f"\nNumber of merged observations: {len(merged)}")
    print(f"Number of countries: {merged['country'].nunique()}")
    print(f"Year range: {merged['year'].min()}-{merged['year'].max()}")


if __name__ == "__main__":
    main()