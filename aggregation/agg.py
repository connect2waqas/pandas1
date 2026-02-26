import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'North', 'South'],
#     'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
#     'Sales': [100, 150, 200, 250, 120, 180, 130, 220],
#     'Quantity': [10, 15, 20, 25, 12, 18, 13, 22],
#     'Date': pd.date_range('2024-01-01', periods=8)
# })

# def region_selling(df):
#     region_sale = df.groupby("Region")["Sales"].agg(["sum","mean","count"])
#     print(region_sale)
# region_selling(df)


# def aggregation(df):
#     stats = df.agg(
#     Total=('Sales', 'sum'),
#     Avg=('Sales', 'mean')
# )
#     print(stats)
# aggregation(df)

# def values_count(df):
#     unique = df[["Region","Product"]].value_counts()
#     return unique

# print(values_count(df))

# def named_agg(df):
#     result = df.groupby("Region").agg(total_Sales = ("Sales", "sum"),
#                                       Avg_Sales = ("Sales", "mean"),
#                                       Total_Qty = ("Quantity","sum")
#                                       )
#     print(result)
# print(named_agg(df))

df = pd.read_csv("imdb-top-1000.csv")
print(df.head(1))
def get_sum_of_genre(df):
    first_methd = df.groupby("Genre").sum()["Gross"].sort_values(ascending=False).head(3)
    second_method =  df.groupby("Genre")["Gross"].sum().sort_values(ascending=False).head(3)
    return df.groupby("Genre")["IMDB_Rating"].mean().sort_values(ascending=False).head(3)


# print(get_sum_of_genre(df))

def get_top_director_by_votes(df):
    top = df.groupby("Director")["No_of_Votes"].max().sort_values(ascending=False).head(1)
    return top
print(get_top_director_by_votes(df))
