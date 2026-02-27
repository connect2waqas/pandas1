from numpy._core.fromnumeric import squeeze
import numpy as np
import pandas as pd
subscriber = pd.read_csv("subs.csv").squeeze()
koli = pd.read_csv("kohli_ipl.csv",index_col="match_no").squeeze()
movie = pd.read_csv("bollywood.csv",index_col="movie").squeeze()


print(type(subscriber.head()))
print(type(koli.head()))
print(type(movie.head()))

def methods():
  print(subscriber.head())
  print(koli.head())
  print(movie.head())
  print(movie.sample()) # it select data randomly. if we pass number than it can give us the that number of value in return. by defult it give one.
  
methods()