# series data structure in pandas
import pandas as pd
print('protein sources')
print('-'*15)
protein= ['egg','peanut','paneer','chicken','protein bar']
series= pd.Series(protein)
print(series)
print(type(protein))

#operations
#retreiving data using intrinsic index
print(series.loc[1])
print(series.loc[3])
#slicing
print(series.loc[3:])
print(series.loc[1:4:2])

#creating a extrinsic index(user defined)
series= pd.Series(protein, index= ['6g','24g','19g','24g','6g'])
print('protein content in the protein sources')
print('-'*40)
print(series)
#retreiving data using intrinsic index
print(series['6g'])
print(series.loc['6g'])
print(series.iloc[3])
# creating series using dictionary
cartype= {'sedan':'civic','SUV':'fortuner','hatchpack':'creta'}
series= pd.Series(cartype)
print('car type')
print('-'*8)
print(series)
print(series['sedan'])
print(series.iloc[2])
print(series.loc['SUV'])
print(type(cartype))



