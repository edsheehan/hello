import pandas as pd
import numpy as np

# Sample application comments
print('Hello World!')

# Sample DataFrame with NaT values
data = {'A': [pd.Timestamp('2024-03-15'), pd.NaT, pd.Timestamp('2024-03-17')],
        'B': [1, 2, np.nan]}

df = pd.DataFrame(data)

print(df.dtypes)

# Replace NaT values with blanks in all columns
df['A'] = df['A'].astype(str)
df.replace(to_replace='NaT', inplace=True, value='')
df.fillna(0, inplace=True)

print(df)

print(df.dtypes)

quit()
