import pandas as pd
import numpy as np
exam_data={
'name': ['Anastasia',
        'Dima',
        'Katherine',
        'James',
        'Emily',
        'Michael',
        'Mathew',
        'Laura',
        'Kevin',
        'Jonas'],
'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts':[1,3,2,3,2,3,1,1,2,1],
'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes'],
'labels':['a','b','c','d','e','f','g','h','i','j']
}
df=pd.DataFrame(exam_data)
df=df.rename(index={i:df['labels'][i] for i in df.index})
df.drop(['labels'],axis=1,inplace=True)
print(df,end='\n+-----------------------------------------+\n')
print(df[(df['attempts']<=2)],end='\n+-----------------------------------------+\n')
