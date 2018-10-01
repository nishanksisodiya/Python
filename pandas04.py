import pandas as pd
import numpy as np
rng=np.random.RandomState(2)
A=pd.DataFrame([[1.0,2.0,3.0],[4,np.nan,np.nan],[7,8,9]])
print(A,end='\n--------------------------------------------\n')
print(A.fillna(A.median(),axis=0),end='\n--------------------------------------------\n')
