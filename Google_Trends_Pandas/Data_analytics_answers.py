import pandas as pd
from pytrends.request import TrendReq 
import matplotlib.pyplot as plt 

dataset = pd.read_csv("Google_Trends_Pandas/Walmart_sales.csv")
print(dataset.shape)
