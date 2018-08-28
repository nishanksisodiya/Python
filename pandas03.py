import pandas as pd,numpy as np
rng=np.random.RandomState(1)
ser=pd.Series(rng.randint(0,10,14))
print(ser)
