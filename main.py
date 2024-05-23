import random
import numpy as np
import pandas as pd

obj = {
    'Argument1': pd.Series(np.arange(1, 101), index=np.arange(1, 101)),
    'Argument2': pd.Series(np.arange(1, 101), index=np.arange(1, 101)),
    'Argument3': pd.Series(np.arange(1, 101), index=np.arange(1, 101))
}
data = pd.DataFrame(obj)

arr = []

for i in range(1, len(data['Argument1'] / 10) + 1):
    for n in range(10):
        arr.append(i)
    if (len(arr) == len(data['Argument1'])):
        break

data['Argument1'] = arr

randInt = random.randint(1, len(data['Argument3']) + 1)

data.loc[(data.index % 10 == 0) & (data.index != 100), 'Argument2'] = randInt

data.to_csv('Calculate.txt', sep='\t', index=False)
