# importing pandas as pd
import pandas as pd
 
# Creating the dataframe
df = pd.read_csv('SQL_and_Tableu/List of Unicorns in the World.csv')
  
# data type are inncorect, need to clean and change

df['Date Joined']= pd.to_datetime(df['Date Joined'])

df.info()

df.to_csv("SQL_and_Tableu/clean_data.csv", index=False)
