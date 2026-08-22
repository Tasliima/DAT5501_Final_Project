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
│   └── test_data_processing.py
├── .gitignore
├── README.md
└── requirements.txt