# importing pandas as pd
import pandas as pd
 
# Creating the dataframe
df = pd.read_csv('VC_Unicorns_Tableau/List of Unicorns in the World.csv')
  
# data type are inncorect, need to clean and change

df['Date Joined']= pd.to_datetime(df['Date Joined'])

df.info()

df.to_csv("VC_Unicorns_Tableau/clean_data.csv", index=False)
