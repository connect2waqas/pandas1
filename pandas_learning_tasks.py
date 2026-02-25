"""
PANDAS LEARNING TASKS - Progressive Learning Path
Dataset: Online Sales Dataset

Complete each task in order. Test your code before moving to the next task.
"""

import pandas as pd

# Load the dataset
df = pd.read_csv(r"online_sales_dataset.csv")

print("="*80)
print("PANDAS LEARNING TASKS - START HERE")
print("="*80)

# ============================================================================
# LEVEL 1: BASIC DATA EXPLORATION (Foundation)
# ============================================================================

# TASK 1: Display first and last rows
# Goal: Understand .head() and .tail() methods
# TODO: Display first 10 rows, then last 10 rows
print("\n--- TASK 1: Display Data ---")
def first_look(df):
    return f"first rows: {df.head(2)}\nlast rows: {df.tail(2)}"
# print(first_look(df))
# TASK 2: Get dataset dimensions
# Goal: Understand .shape, .info(), .columns, .index
# TODO: Print the shape, column names, and number of rows
print("\n--- TASK 2: Dataset Dimensions ---")
# Your code here:
def get_data_dimension(df):
    rows , columns = df.shape
    print(f"Number of rows : {rows}\nNumber of columns: {columns}")
    print(f"Columns names in our data is : {df.columns.tolist()}")
    print(f"Number of rows in our data is : {df.index}")
    return df.info()
# get_data_dimension(df)

# TASK 3: Check data types
# Goal: Understand .dtypes and .info()
# TODO: Display data types of all columns
# TODO: How many numeric columns? How many object columns?
print("\n--- TASK 3: Data Types ---")
def data_types(df):
    print(df.dtypes)
    numeric_columns = len(df.select_dtypes(include="number").columns)
    non_numeric_count = len(df.select_dtypes(exclude='number').columns)
    return f"Number of numeric columns are : {numeric_columns}\nNumber of non-numeric columns are: {non_numeric_count}"
# print(data_types(df))
# TASK 4: Get basic statistics
# Goal: Understand .describe() for numeric and categorical data
# TODO: Get statistics for numeric columns
# TODO: Get statistics for object columns using describe(include='object')
print("\n--- TASK 4: Basic Statistics ---")
def basic_statistics(df):
    return df.describe()
# print(basic_statistics(df))
# ============================================================================
# LEVEL 2: SELECTING AND ACCESSING DATA
# ============================================================================

# TASK 5: Select single column
# Goal: Understand df['column'] vs df.column
# TODO: Select and display first 10 values of 'Country' column
print("\n--- TASK 5: Single Column Selection ---")
def single_column(df):
    invoice_no= df["InvoiceNo"].head(5) # select only first five invoice columns 
    print(f"Invoice columns:\n{invoice_no}")
    # we can also do it through the following 
    # print(df["InvoiceNo"])


# TASK 6: Select multiple columns
# Goal: Understand df[['col1', 'col2']]
# TODO: Select 'InvoiceNo', 'Description', 'Quantity', 'UnitPrice', 'Country'
# TODO: Display first 10 rows
print("\n--- TASK 6: Multiple Column Selection ---")
def multiple_columns_selections(df):
    print(df[["InvoiceNo","Description","Quantity","UnitPrice","Country"]].head(5))
    selected = df[["InvoiceNo","Description","Quantity","UnitPrice","Country"]]
    print(selected.head(5))
# multiple_columns_selections(df)
# TASK 7: Select rows using .iloc[]
# Goal: Understand position-based indexing
# TODO: Select rows 10 to 20 using .iloc
# TODO: Select first 5 rows and first 5 columns using .iloc
print("\n--- TASK 7: Position-Based Selection ---")
# Your code here:


# TASK 8: Select rows using .loc[]
# Goal: Understand label-based indexing
# TODO: Select rows where index is between 0 and 10
# TODO: Select specific rows and specific columns
print("\n--- TASK 8: Label-Based Selection ---")
# Your code here:


# ============================================================================
# LEVEL 3: FILTERING DATA (Conditional Selection)
# ============================================================================

# TASK 9: Simple filtering
# Goal: Filter rows based on one condition
# TODO: Get all sales from 'United Kingdom'
# TODO: Get all sales where Quantity > 30
print("\n--- TASK 9: Simple Filtering ---")
# Your code here:


# TASK 10: Multiple conditions (AND)
# Goal: Combine conditions with &
# TODO: Get sales from 'United Kingdom' AND Quantity > 30
# TODO: Remember to use parentheses around each condition
print("\n--- TASK 10: Multiple Conditions (AND) ---")
# Your code here:


# TASK 11: Multiple conditions (OR)
# Goal: Combine conditions with |
# TODO: Get sales from 'United Kingdom' OR 'Germany'
# TODO: Get sales where Quantity > 40 OR UnitPrice > 90
print("\n--- TASK 11: Multiple Conditions (OR) ---")
# Your code here:


# TASK 12: Using .isin() method
# Goal: Filter based on list of values
# TODO: Get sales from ['United Kingdom', 'Germany', 'France', 'Spain']
# TODO: Get sales where Category is in ['Electronics', 'Furniture']
print("\n--- TASK 12: Using .isin() ---")
# Your code here:


# TASK 13: String filtering
# Goal: Use .str methods for string operations
# TODO: Find all products where Description contains 'USB'
# TODO: Find all countries that start with 'U'
print("\n--- TASK 13: String Filtering ---")
# Your code here:


# ============================================================================
# LEVEL 4: HANDLING MISSING DATA
# ============================================================================

# TASK 14: Detect missing values
# Goal: Use .isnull(), .isna(), .notna()
# TODO: Count missing values in each column
# TODO: Find rows where CustomerID is missing
print("\n--- TASK 14: Detect Missing Values ---")
# Your code here:


# TASK 15: Drop missing values
# Goal: Use .dropna()
# TODO: Create a new dataframe without any missing values
# TODO: Drop rows where only 'CustomerID' is missing
print("\n--- TASK 15: Drop Missing Values ---")
# Your code here:


# TASK 16: Fill missing values
# Goal: Use .fillna()
# TODO: Fill missing CustomerID with 0
# TODO: Fill missing ShippingCost with the mean value
print("\n--- TASK 16: Fill Missing Values ---")
# Your code here:


# ============================================================================
# LEVEL 5: ADDING AND MODIFYING COLUMNS
# ============================================================================

# TASK 17: Create new column (simple calculation)
# Goal: Create calculated columns
# TODO: Create 'TotalPrice' = Quantity * UnitPrice
# TODO: Create 'FinalPrice' = TotalPrice - (TotalPrice * Discount)
print("\n--- TASK 17: Create Calculated Columns ---")
# Your code here:


# TASK 18: Modify existing column
# Goal: Transform column values
# TODO: Convert all Country names to uppercase
# TODO: Round UnitPrice to 2 decimal places
print("\n--- TASK 18: Modify Columns ---")
# Your code here:


# TASK 19: Conditional column creation
# Goal: Use np.where() or .apply()
# TODO: Create 'PriceCategory': 'Expensive' if UnitPrice > 50, else 'Affordable'
# TODO: Create 'OrderSize': 'Large' if Quantity > 30, 'Small' otherwise
print("\n--- TASK 19: Conditional Columns ---")
import numpy as np
# Your code here:


# TASK 20: Apply custom function
# Goal: Use .apply() with custom function
# TODO: Create function to categorize shipping cost (Low: <10, Medium: 10-20, High: >20)
# TODO: Apply it to create 'ShippingCategory' column
print("\n--- TASK 20: Apply Custom Function ---")
# Your code here:


# ============================================================================
# LEVEL 6: SORTING AND RANKING
# ============================================================================

# TASK 21: Sort by single column
# Goal: Use .sort_values()
# TODO: Sort by UnitPrice in descending order
# TODO: Display top 10 most expensive products
print("\n--- TASK 21: Sort by Single Column ---")
# Your code here:


# TASK 22: Sort by multiple columns
# Goal: Sort with multiple criteria
# TODO: Sort by Country (ascending) and then UnitPrice (descending)
print("\n--- TASK 22: Sort by Multiple Columns ---")
# Your code here:


# TASK 23: Ranking data
# Goal: Use .rank() method
# TODO: Create rank for UnitPrice (1 = highest price)
# TODO: Find the rank of each product within its category
print("\n--- TASK 23: Ranking ---")
# Your code here:


# ============================================================================
# LEVEL 7: GROUPING AND AGGREGATION (Most Important!)
# ============================================================================

# TASK 24: Simple groupby with single aggregation
# Goal: Understand .groupby() basics
# TODO: Calculate total quantity sold per Country
# TODO: Calculate average UnitPrice per Category
print("\n--- TASK 24: Simple Groupby ---")
# Your code here:


# TASK 25: Groupby with multiple aggregations
# Goal: Use .agg() for multiple calculations
# TODO: For each Country, calculate: total Quantity, average UnitPrice, total orders
print("\n--- TASK 25: Multiple Aggregations ---")
# Your code here:


# TASK 26: Groupby with multiple columns
# Goal: Group by more than one column
# TODO: Calculate total quantity sold per Country AND Category
# TODO: Calculate average price per PaymentMethod AND Category
print("\n--- TASK 26: Multiple Column Groupby ---")
# Your code here:


# TASK 27: Advanced aggregations
# Goal: Use different functions for different columns
# TODO: Group by Country and calculate:
#       - sum of Quantity
#       - mean of UnitPrice
#       - count of InvoiceNo
#       - max of ShippingCost
print("\n--- TASK 27: Advanced Aggregations ---")
# Your code here:


# ============================================================================
# LEVEL 8: MERGING AND COMBINING DATA
# ============================================================================

# TASK 28: Value counts
# Goal: Use .value_counts()
# TODO: Count how many sales per Country
# TODO: Count how many sales per PaymentMethod
# TODO: Get percentage distribution
print("\n--- TASK 28: Value Counts ---")
# Your code here:


# TASK 29: Unique values
# Goal: Use .unique() and .nunique()
# TODO: Find all unique Countries
# TODO: Count number of unique products (Description)
print("\n--- TASK 29: Unique Values ---")
# Your code here:


# TASK 30: Crosstab / Pivot Table
# Goal: Create summary tables
# TODO: Create crosstab of Country vs Category (count of sales)
# TODO: Create pivot table showing average UnitPrice by Country and Category
print("\n--- TASK 30: Crosstab and Pivot ---")
# Your code here:


# ============================================================================
# LEVEL 9: DATE AND TIME OPERATIONS
# ============================================================================

# TASK 31: Convert to datetime
# Goal: Use pd.to_datetime()
# TODO: Convert InvoiceDate to datetime type
# TODO: Extract year, month, day, hour into separate columns
print("\n--- TASK 31: DateTime Conversion ---")
# Your code here:


# TASK 32: Date filtering
# Goal: Filter based on dates
# TODO: Get all sales from January 2020
# TODO: Get all sales from a specific day
print("\n--- TASK 32: Date Filtering ---")
# Your code here:


# TASK 33: Date aggregations
# Goal: Group by time periods
# TODO: Calculate total sales per month
# TODO: Calculate average order value per day
print("\n--- TASK 33: Date Aggregations ---")
# Your code here:


# ============================================================================
# LEVEL 10: DATA CLEANING AND VALIDATION
# ============================================================================

# TASK 34: Detect outliers
# Goal: Find unusual values
# TODO: Find rows where Quantity is negative
# TODO: Find rows where Discount > 1.0 (invalid discount)
print("\n--- TASK 34: Detect Outliers ---")
# Your code here:


# TASK 35: Remove duplicates
# Goal: Use .duplicated() and .drop_duplicates()
# TODO: Check if there are any duplicate rows
# TODO: Remove duplicate InvoiceNo if any
print("\n--- TASK 35: Handle Duplicates ---")
# Your code here:


# TASK 36: Data validation
# Goal: Validate data integrity
# TODO: Check for negative UnitPrice values
# TODO: Check for missing critical fields (InvoiceNo, StockCode)
# TODO: Verify all Discounts are between 0 and 1
print("\n--- TASK 36: Data Validation ---")
# Your code here:


# ============================================================================
# LEVEL 11: ADVANCED OPERATIONS
# ============================================================================

# TASK 37: Bins and categories
# Goal: Use pd.cut() and pd.qcut()
# TODO: Create price ranges: Low (0-30), Medium (30-60), High (60+)
# TODO: Create 4 equal-sized groups based on Quantity (quartiles)
print("\n--- TASK 37: Binning Data ---")
# Your code here:


# TASK 38: Window functions
# Goal: Use .rolling() and .expanding()
# TODO: Calculate 3-day moving average of sales
print("\n--- TASK 38: Rolling Calculations ---")
# Your code here:


# TASK 39: String operations
# Goal: Master .str methods
# TODO: Extract country code (first 3 letters)
# TODO: Convert Description to title case
# TODO: Check if Description contains 'Desk' or 'Chair'
print("\n--- TASK 39: String Operations ---")
# Your code here:


# TASK 40: Export data
# Goal: Save processed data
# TODO: Save cleaned data to new CSV
# TODO: Export summary statistics to Excel (if openpyxl installed)
print("\n--- TASK 40: Export Data ---")
# Your code here:
# df.to_csv('cleaned_sales_data.csv', index=False)

print("\n" + "="*80)
print("CONGRATULATIONS! You've completed all Pandas learning tasks!")
print("="*80)
