# Retail Sales Analysis Project

This project demonstrates a data analysis workflow for retail sales data. It includes data preprocessing in Python and SQL queries for generating insights from the data.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup and Installation](#setup-and-installation)
- [Data Preprocessing](#data-preprocessing)
- [SQL Queries for Analysis](#sql-queries-for-analysis)
- [Results](#results)
- [Contact](#contact)

## Project Overview
The goal of this project is to analyze a dataset containing retail order information. Using Python, we preprocess and clean the data, then load it into a SQL Server database. SQL queries are then used to perform analytics on the data, such as identifying top-selling products, calculating month-over-month growth, and determining high-growth subcategories.

## Setup and Installation

### Prerequisites
1. Python 3.x
2. SQL Server (local or remote)
3. Kaggle API (for downloading the dataset)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-github-username/retail-sales-analysis.git
    cd retail-sales-analysis
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset using Kaggle:
    ```bash
    kaggle datasets download ankitbansal06/retail-orders -f orders.csv
    ```

4. Run the Python script to preprocess and load data into SQL Server:
    ```bash
    python data_preprocessing.py
    ```

## Data Preprocessing

The data preprocessing script `data_preprocessing.py`:
1. Downloads the dataset from Kaggle.
2. Extracts the file from a compressed zip format.
3. Loads the data using pandas and handles null values.
4. Renames columns for consistency.
5. Calculates new columns for discount, sale price, and profit.
6. Converts the order date to a datetime format.
7. Loads the cleaned data into a SQL Server table.

## SQL Queries for Analysis

The `sql_queries.sql` file includes SQL scripts for analyzing the processed data. Key analyses include:
1. **Top 10 Revenue-Generating Products:** Find the top 10 products based on total sales.
2. **Top 5 Selling Products by Region:** Identify the top 5 products with the highest sales in each region.
3. **Month-over-Month Growth Comparison:** Compare monthly sales for 2022 and 2023.
4. **Highest Sales by Month for Each Category:** Determine the month with the highest sales for each product category.
5. **Subcategory with Highest Growth:** Identify the subcategory with the largest profit growth from 2022 to 2023.

## Results

The insights generated through these SQL queries help understand product performance, regional preferences, sales trends, and growth across different product categories. For instance:
- **Top Revenue Products:** These insights can guide marketing efforts to promote best-sellers.
- **Regional Bestsellers:** Help regional managers make informed decisions based on popular products.
- **Sales Growth Comparison:** Track and plan for seasonality or changes in demand.

## Contact

For any questions or collaboration, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/naraharisetty-lahari-siva-prasad-a369a2335).

---

This project was developed for educational purposes and showcases data analysis skills using Python and SQL.
