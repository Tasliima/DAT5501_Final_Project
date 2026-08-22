import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.api as sm

from data_processing import (
    load_working_hours,
    load_productivity,
    merge_datasets,
)


def prepare_data():
    hours = load_working_hours("data/annual-working-hours-per-worker.csv")
    productivity = load_productivity("data/labour-productivity.csv")
    return merge_datasets(hours, productivity)


def correlation_analysis(df):
    correlation, p_value = pearsonr(
        df["annual_working_hours"],
        df["productivity_per_hour"],
    )

    print(f"Pearson correlation: {correlation:.3f}")
    print(f"P-value: {p_value:.5f}")

    return correlation, p_value


def regression_analysis(df):
    x = df["annual_working_hours"]
    y = df["productivity_per_hour"]

    x = sm.add_constant(x)

    model = sm.OLS(y, x).fit()

    print("\nRegression results:")
    print(model.summary())

    return model

def recent_analysis(df):
    """Analyse the relationship using observations from 2000 onwards."""
    recent = df[df["year"] >= 2000].copy()

    correlation, p_value = pearsonr(
        recent["annual_working_hours"],
        recent["productivity_per_hour"],
    )

    x = sm.add_constant(recent["annual_working_hours"])
    y = recent["productivity_per_hour"]
    model = sm.OLS(y, x).fit()

    print("\n--- Recent period analysis: 2000-2019 ---")
    print(f"Observations: {len(recent)}")
    print(f"Countries: {recent['country'].nunique()}")
    print(f"Pearson correlation: {correlation:.3f}")
    print(f"P-value: {p_value:.5f}")
    print(f"R-squared: {model.rsquared:.3f}")
    print(
        "Working hours coefficient: "
        f"{model.params['annual_working_hours']:.4f}"
    )

    return recent, model

def country_comparison(df):
    """Compare average working hours and productivity by country since 2000."""
    recent = df[df["year"] >= 2000].copy()

    country_summary = (
        recent.groupby("country")
        .agg(
            average_working_hours=("annual_working_hours", "mean"),
            average_productivity=("productivity_per_hour", "mean"),
        )
        .reset_index()
    )

    # Countries with the shortest average working hours
    shortest = country_summary.nsmallest(10, "average_working_hours")

    # Countries with the longest average working hours
    longest = country_summary.nlargest(10, "average_working_hours")

    print("\n--- 10 countries with shortest working hours ---")
    print(shortest.to_string(index=False))

    print("\n--- 10 countries with longest working hours ---")
    print(longest.to_string(index=False))

    country_summary.to_csv(
        "data/country_summary_2000_2019.csv",
        index=False,
    )

    return country_summary

def create_scatter_plot(df):
    plt.figure(figsize=(9, 6))

    plt.scatter(
        df["annual_working_hours"],
        df["productivity_per_hour"],
        alpha=0.4,
    )

    plt.xlabel("Annual working hours per worker")
    plt.ylabel("Productivity per hour worked")
    plt.title("Annual Working Hours vs Labour Productivity")

    plt.tight_layout()
    plt.savefig("figures/hours_vs_productivity.png", dpi=300)
    plt.close()


def create_recent_country_plot(df):
    recent = df[df["year"] >= 2000]

    country_average = (
        recent.groupby("country")[
            ["annual_working_hours", "productivity_per_hour"]
        ]
        .mean()
        .reset_index()
    )

    plt.figure(figsize=(9, 6))

    plt.scatter(
        country_average["annual_working_hours"],
        country_average["productivity_per_hour"],
        alpha=0.7,
    )

    plt.xlabel("Average annual working hours")
    plt.ylabel("Average productivity per hour")
    plt.title("Average Working Hours vs Productivity, 2000-2019")

    plt.tight_layout()
    plt.savefig("figures/country_average_2000_2019.png", dpi=300)
    plt.close()


def main():
    df = prepare_data()

    print(f"Observations: {len(df)}")
    print(f"Countries: {df['country'].nunique()}")

    correlation_analysis(df)
    regression_analysis(df)
    recent_analysis(df)
    country_comparison(df)

    create_scatter_plot(df)
    create_recent_country_plot(df)

    print("\nFigures saved successfully.")


if __name__ == "__main__":
    main()