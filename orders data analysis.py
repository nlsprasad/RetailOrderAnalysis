# Import necessary libraries
import pandas as pd
import zipfile
import sqlalchemy as sal

# Step 1: Extract the dataset from the zip file
def extract_zip(zip_filename, extract_to="."):
    """
    Extracts the specified zip file to the given directory.

    Args:
    zip_filename (str): The path to the zip file.
    extract_to (str): The directory where the files should be extracted. Defaults to the current directory.
    """
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"{zip_filename} extracted to {extract_to}")

# Extracting 'orders.csv.zip' to the current directory
extract_zip('orders.csv.zip')

# Step 2: Load and clean the data
def load_and_clean_data(filename):
    """
    Loads data from a CSV file and handles missing values by replacing specified null values.

    Args:
    filename (str): The path to the CSV file.

    Returns:
    DataFrame: A cleaned DataFrame with modified column names.
    """
    df = pd.read_csv(filename, na_values=['Not Available', 'unknown'])
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    print("Columns renamed to lowercase with underscores.")
    return df

# Loading and cleaning the data
df = load_and_clean_data('orders.csv')
print("Unique shipping modes:", df['ship_mode'].unique())
print(df.head())

# Step 3: Add calculated columns (discount, sale price, profit)
def add_calculated_columns(df):
    """
    Adds discount, sale_price, and profit columns to the DataFrame.

    Args:
    df (DataFrame): The input DataFrame with required columns.

    Returns:
    DataFrame: The modified DataFrame with new calculated columns.
    """
    df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
    df['sale_price'] = df['list_price'] - df['discount']
    df['profit'] = df['sale_price'] - df['cost_price']
    return df

# Adding the calculated columns
df = add_calculated_columns(df)
print("Calculated columns added.")
print(df.head())

# Step 4: Convert order_date to datetime format
df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")
print("Order date column converted to datetime.")

# Step 5: Drop unnecessary columns
def drop_unnecessary_columns(df, columns):
    """
    Drops specified columns from the DataFrame.

    Args:
    df (DataFrame): The input DataFrame.
    columns (list): List of column names to drop.

    Returns:
    DataFrame: The modified DataFrame without the specified columns.
    """
    df.drop(columns=columns, inplace=True)
    print(f"Columns {columns} dropped.")
    return df

# Dropping 'list_price', 'cost_price', and 'discount_percent' columns
df = drop_unnecessary_columns(df, ['list_price', 'cost_price', 'discount_percent'])
print(df.head())

# Step 6: Load the data into SQL Server
def load_data_to_sql(df, table_name, connection_string, if_exists='append'):
    """
    Loads the DataFrame into an SQL Server table.

    Args:
    df (DataFrame): The DataFrame to load.
    table_name (str): The name of the target SQL table.
    connection_string (str): SQLAlchemy connection string for SQL Server.
    if_exists (str): Behavior for existing tables ('replace' or 'append').
    """
    engine = sal.create_engine(connection_string)
    with engine.connect() as conn:
        df.to_sql(table_name, con=conn, index=False, if_exists=if_exists)
    print(f"Data loaded into SQL table {table_name} with if_exists='{if_exists}'")

# Define the connection string and table name
connection_string = 'mssql://ANKIT\\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER'
table_name = 'df_orders'

# Load data to SQL
load_data_to_sql(df, table_name, connection_string)



