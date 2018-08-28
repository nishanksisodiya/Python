import pandas as pd
import numpy as np
d1={'India':1300000000,'California':4595245,'Texas':2232854,'Manchester':552255,'San Jose':8454441}
d2={'India':15305,'California':4455,'Texas':2254,'Manchester':5522,'San Jose':84541}
d3={'India':1530,'California':455,'Texas':224,'Manchester':522,'San Jose':8441}
df=pd.DataFrame({'pop':d1,'ar':d2})
df['den']=None
print(df,end='\n--------------------------------------------\n')
for i in df.index:
    df['den'][i]=d3[i]
df.loc['Paris']=[120000,23000,3400]
print(df,end='\n--------------------------------------------\n')
df=df.rename(index={"Paris": "Moscow"})
print(df,end='\n--------------------------------------------\n')
print(df[(df['pop']>840000) & (df['pop']<1000000000)])
