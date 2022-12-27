#importing libraries
import csv
import pandas as pd

data = pd.read_csv("daily_sales_data_0.csv") #read the csv file
ds = pd.DataFrame(data) #load using panda dataframe
dt = ds[ds['product'] == "pink morsel"] #isolate pink morsel

dmSales = dt['quantity'] * dt['price'].str[1:].astype(float) #function for calcultion the sales
dmSales= "$"+dmSales.astype(str)  #inserting the dollar character

nhead={'Sales':dmSales,'Date':dt['date'], 'Region':dt['region']} #assigning data to table
ntable = pd.DataFrame(nhead) #load as panda dataframe

#display new table
print(ntable) 
