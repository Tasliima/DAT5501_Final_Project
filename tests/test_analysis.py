import pandas as pd

from src.analysis import (
    correlation_analysis,
    regression_analysis,
    country_comparison,
    calculate_country_changes,
)


def sample_data():
    """Create a small dataset for analysis testing."""
    return pd.DataFrame(
        {
            "country": [
                "Country A", "Country A",
                "Country B", "Country B",
                "Country C", "Country C",
            ],
            "year": [
                2000, 2019,
                2000, 2019,
                2000, 2019,
            ],
            "annual_working_hours": [
                2000, 1800,
                1800, 1700,
                1600, 1500,
            ],
            "productivity_per_hour": [
                20, 30,
                40, 50,
                60, 70,
            ],
        }
    )


def test_correlation_analysis():
    df = sample_data()

    correlation, p_value = correlation_analysis(df)

    assert -1 <= correlation <= 1
    assert 0 <= p_value <= 1
    assert correlation < 0


def test_regression_analysis():
    df = sample_data()

    model = regression_analysis(df)

    assert "annual_working_hours" in model.params.index
    assert model.params["annual_working_hours"] < 0
    assert 0 <= model.rsquared <= 1


def test_country_comparison(tmp_path, monkeypatch):
    df = sample_data()

    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()

    result = country_comparison(df)

    assert len(result) == 3
    assert "average_working_hours" in result.columns
    assert "average_productivity" in result.columns

    assert (
        tmp_path / "data" / "country_summary_2000_2019.csv"
    ).exists()


def test_calculate_country_changes(tmp_path, monkeypatch):
    df = sample_data()

    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()

    result = calculate_country_changes(df)

    assert len(result) == 3
    assert "hours_change" in result.columns
    assert "productivity_change" in result.columns

    assert (
        tmp_path / "data" / "country_changes_2000_2019.csv"
    ).exists()