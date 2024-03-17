# Sample application comments
print ('Hello World!')

import pandas as pd
import numpy as np

# Sample DataFrame with NaT values
data = {'A': [pd.Timestamp('2024-03-15'), pd.NaT, pd.Timestamp('2024-03-17')],
        'B': [1, 2, np.nan]}
df = pd.DataFrame(data)

# Replace NaT values with blanks in all columns
df_cleaned = df.fillna('')

print(df_cleaned)


quit()