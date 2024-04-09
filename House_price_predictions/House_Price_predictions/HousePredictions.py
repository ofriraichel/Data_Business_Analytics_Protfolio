# Set up filepaths
import os

# Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#import data files
if not os.path.exists("/Users/ofriraichel/ML projects/House_price_predictions/House_Price_predictions/home-data-for-ml-course/train.csv"):
    os.symlink("..home-data-for-ml-course/train.csv", "..home-data-for-ml-course/train.csv")  
    os.symlink("..home-data-for-ml-course/test.csv", "..home-data-for-ml-course/test.csv") 

# Load the data, and separate the target
iowa_file_path = '/Users/ofriraichel/ML projects/House_price_predictions/House_Price_predictions/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice

# Create X 
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select columns corresponding to features, and preview the data
X = home_data[features]
X.head()

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define a random forest model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

# To improve accuracy, created a new Random Forest model
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X,y)

# path to file you will use for predictions
test_data_path = '/Users/ofriraichel/ML projects/House_price_predictions/House_Price_predictions/home-data-for-ml-course/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]
# make predictions. 
test_preds = rf_model_on_full_data.predict(test_X)

print(test_preds)




