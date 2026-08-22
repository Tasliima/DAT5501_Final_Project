import pandas as pd

from src.data_processing import (
    load_working_hours,
    load_productivity,
    merge_datasets,
)


def test_load_working_hours(tmp_path):
    test_data = pd.DataFrame(
        {
            "Entity": ["Country A", "Country B"],
            "Year": [2018, 2019],
            "Working hours per worker": [1800, 1600],
        }
    )

    filepath = tmp_path / "hours.csv"
    test_data.to_csv(filepath, index=False)

    result = load_working_hours(filepath)

    assert list(result.columns) == [
        "country",
        "year",
        "annual_working_hours",
    ]
    assert len(result) == 2
    assert result.iloc[0]["annual_working_hours"] == 1800


def test_load_productivity(tmp_path):
    test_data = pd.DataFrame(
        {
            "Entity": ["Country A", "Country B"],
            "Code": ["AAA", "BBB"],
            "Year": [2018, 2019],
            "Productivity: output per hour worked": [40.5, 55.2],
        }
    )

    filepath = tmp_path / "productivity.csv"
    test_data.to_csv(filepath, index=False)

    result = load_productivity(filepath)

    assert list(result.columns) == [
        "country",
        "year",
        "productivity_per_hour",
    ]
    assert len(result) == 2
    assert result.iloc[1]["productivity_per_hour"] == 55.2


def test_merge_datasets():
    hours = pd.DataFrame(
        {
            "country": ["Country A", "Country B"],
            "year": [2019, 2019],
            "annual_working_hours": [1500, 2000],
        }
    )

    productivity = pd.DataFrame(
        {
            "country": ["Country A", "Country B"],
            "year": [2019, 2019],
            "productivity_per_hour": [70, 30],
        }
    )

    result = merge_datasets(hours, productivity)

    assert len(result) == 2
    assert "annual_working_hours" in result.columns
    assert "productivity_per_hour" in result.columns


def test_merge_removes_missing_values():
    hours = pd.DataFrame(
        {
            "country": ["Country A", "Country B"],
            "year": [2019, 2019],
            "annual_working_hours": [1500, None],
        }
    )

    productivity = pd.DataFrame(
        {
            "country": ["Country A", "Country B"],
            "year": [2019, 2019],
            "productivity_per_hour": [70, 30],
        }
    )

    result = merge_datasets(hours, productivity)

    assert len(result) == 1
    assert result.iloc[0]["country"] == "Country A"