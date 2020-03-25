# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 01:14:33 2020

@author: sydne
"""

import pandas as pd

# Imports a local CSV that contains the property value data for every 
# residential (single-family, townhouse, or rowhouse) property sale  in Allegheny County. 
# Each row contains the municipality, municipal code, property sale value, and year of sale for each residential property.
data = pd.DataFrame.from_csv('PropertyValues.csv')

# creates a pandas series of property valyes by aggregating by municipality, municipal code and sale year
# (note that there is no discrepancy between municipality and municode - each municipality has 
# one and only one municode and vice versa - the municode is included for the purpose of joining with 
# geospatial data during the GIS mapping process)
# returns the average sale price per municipality per year
annualPValues = data.groupby(['MUNICIPALITY','MUNICODE', 'SALEYEAR'])['SALEPRICE'].mean()

# coverts the pandas series to a pandas dataframe
dframe = annualPValues.to_frame()

# creates a new column that copies the municipality, municipal code, and sale year 
# (which is currently stored in the index and thus doesn't get included in the CSV file)
dframe['index1'] = dframe.index

# resets the index of the dataframe
dframe = dframe.reset_index(drop = True)

# splits the data (the municipality, municipal code, and sale year) in the index1 column 
# into three separate columns 
dframe[['MUNICIPALITY', 'MUNICODE', 'YEAR']] = pd.DataFrame(dframe['index1'].tolist(), index = dframe.index)

# exports the dataframe to a CSV
# Columns = municipality, municode, year, and average annual property valye
dframe.to_csv(r'C:\Users\sydne\OneDrive\Desktop\Heinz\S20\GIS\Project\AnnualPropertyValuesMunicipalities.csv', index = False)