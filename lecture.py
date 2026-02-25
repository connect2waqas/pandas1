import pandas as pd

path = r"C:\Users\ztech.pk\OneDrive\Desktop\pandas1\online_sales_dataset.csv"

data = path.replace("\\","/")

df = pd.read_csv(data)

def look_up_to_data(df):
    return f"First five rows:\n{df.head(5)} \nFirst last rows:\n{df.tail(5)}"

print(look_up_to_data(df))

def shape_of_data(df):
    rows, columns = df.shape
    return f"row are: {rows} \ncolumns are: {columns}"

# print(shape_of_data(df))

