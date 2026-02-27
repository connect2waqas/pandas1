import numpy as np
import pandas as pd

marks =  [45,85,94,50]
subject = ["English","Data Science","maths","science"]
df  = pd.Series(marks,index=subject,name = "Marks of Waqas")


def attributes_of_series(df):
    # size = type(df.size)
    # name = type(df.name)
    # data_type = type(df.dtype)
    # unique = type(df.is_unique)
    # index_values = type(df.index)
    # values = type(df.values)
    print(df.index)
    print(locals())

attributes_of_series(df)
