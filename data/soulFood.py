#importing libraries
import csv
import pandas as pd

data1 = pd.read_csv("daily_sales_data_0.csv") #read the csv file
data2 = pd.read_csv("daily_sales_data_1.csv")
data3 = pd.read_csv("daily_sales_data_2.csv")
con = pd.concat(map(pd.read_csv,['daily_sales_data_0.csv',
                'daily_sales_data_1.csv', 
                'daily_sales_data_2.csv']
                ))
ds = pd.DataFrame(con)  # load using panda dataframe
dt = ds[ds['product'] == "pink morsel"] #isolate pink morsel

dmSales = dt['quantity'] * dt['price'].str[1:].astype(float) #function for calcultion the sales
dmSales= "$"+dmSales.astype(str)  #inserting the dollar character

nhead={'Sales':dmSales,'Date':dt['date'], 'Region':dt['region']} #assigning data to table
ntable = pd.DataFrame(nhead) #load as panda dataframe

#display new table
print(ntable) 
