import pandas as pd
import numpy

protein= {'protein source':['yogurt','milk','chicken'
                            ,'peanut','soya chunks',
                            'paneer'],
          'protein per 100gms':['19gms','11gms','24gms',
                                '25gms','52gms','22gms']}
df=pd.DataFrame(protein)
print(df)
#intrinsic indexing
print(df.loc[3])

#extrinsic indexing
df=pd.DataFrame(protein,index=['source1','source2','source3','source4','source5','source6'])
print(df)
print(df.loc['source1'])
print(df.iloc[3])

#adding a column
df['source type']= ['veg','veg','non-veg','vegan','vegan','veg']
print(df)

df['price']=['25rs','7rs','20rs','20rs','20rs','65rs']
print(df)

#adding a row
source7= pd.DataFrame({'protein source':'pea','protein per 100gms':'8gms','source type':'vegan','price':'15rs'},
                      index=['source7'])
df=pd.concat([df,source7])
print(df)

print("First 6 rows:")
print(df.head(6))
print("Last 4 rows:")
print(df.tail(4))
print("Statistical Summary:")
print(df.describe())







