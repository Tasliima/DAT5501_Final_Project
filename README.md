# Annual Working Hours and Labour Productivity

## Project Overview

Hello!

This project investigates the relationship between annual working hours and labour productivity across countries.

The analysis examines whether countries with shorter average working hours tend to demonstrate higher levels of productivity per hour worked. It uses international country-level data covering working hours and labour productivity.

## Research Question

**Are shorter annual working hours associated with higher labour productivity across countries?**

## Data

The project uses two datasets:

1. **Annual Working Hours per Worker**
   - Contains annual working hours by country and year.
   - Source: Our World in Data.

2. **Labour Productivity per Hour Worked**
   - Contains estimates of economic output per hour worked by country and year.
   - Source: Our World in Data / Penn World Table.

The datasets are merged using country and year.

## Methods

The analysis includes:

- Data cleaning and preparation
- Dataset merging
- Exploratory data analysis
- Pearson correlation analysis
- Ordinary Least Squares (OLS) regression
- Recent-period analysis for 2000–2019
- Country-level comparisons
- Data visualisation

## Project Structure

```text
DAT5501_Final_Project/
├── .circleci/
│   └── config.yml
├── data/
├── figures/
├── report/
├── src/
│   ├── analysis.py
│   └── data_processing.py
├── tests/
│   ├── test_analysis.py
│   └── test_data_processing.py
├── .gitignore
├── README.md
└── requirements.txt```

## Installation

Install the required Python packages from the project root:

```bash
python3 -m pip install -r requirements.txt
```

## Running the Analysis

Run the complete analysis from the project root using:

```bash
python3 -m src.analysis
```

The analysis outputs summary statistics and statistical results to the terminal. Generated visualisations are saved in the `figures` directory, while derived country-level datasets are saved in the `data` directory.

## Running the Tests

Run all unit tests using:

```bash
python3 -m pytest -v
```

The test suite covers data loading, data cleaning and merging, correlation analysis, regression analysis, country comparisons and country-level change calculations.

## Continuous Integration

CircleCI is configured in `.circleci/config.yml`. The continuous integration workflow installs the project dependencies and automatically runs the test suite.

## Key Findings

The full dataset contains 3,457 matched observations across 69 countries between 1950 and 2019.

The initial analysis identifies a strong negative association between annual working hours and labour productivity. Across the full dataset, the Pearson correlation is approximately -0.690.

Analysis restricted to 2000–2019 produces a similar correlation of approximately -0.686, suggesting that the overall cross-country relationship is also present in more recent observations.

However, analysis of changes within individual countries between 2000 and 2019 produces a substantially weaker correlation of approximately -0.168, which is not statistically significant. The findings therefore demonstrate an association between working hours and productivity across countries but do not establish that reducing working hours causes productivity to increase.

## Limitations

The analysis is observational and should not be interpreted as evidence of causation. Differences in economic development, industry composition, technology, labour-market structures and other country-level characteristics may influence both working hours and productivity.

## Repository Contents

- `src/data_processing.py` — data loading, cleaning and merging functions.
- `src/analysis.py` — statistical analysis and visualisation functions.
- `tests/test_data_processing.py` — unit tests for the data-processing pipeline.
- `tests/test_analysis.py` — unit tests for analytical functions.
- `figures/` — generated visualisations.
- `data/` — source and derived datasets.
- `.circleci/config.yml` — continuous integration configuration.