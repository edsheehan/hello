import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Define a function to calculate the support state of an app based on support dates
def support_state(row):
    td = pd.Timestamp.today().normalize()
    if row['End of Extended Support'] < td and row['End of Extended Support'] is not pd.NaT:
        return 'Out of Support'
    if row['End of Support'] < td and row['End of Support'] is not pd.NaT and row['End of Extended Support'] is pd.NaT:
        return 'Out of Support'
    elif row['End of Support'] < td and row['End of Support'] is not pd.NaT:
        return 'Extended Support'
    elif row['General Availability'] < td and row['General Availability'] is not pd.NaT:
        return 'Normal Support'
    else:
        return 'Undefined'

# Define the file path of the CSV file containing the data
file_path = 'C:/Users/ed/OneDrive/Documents/software.csv'

# Read CSV file into pandas DataFrame
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime format and sort by 'AppID' and 'Date' columns
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y').dt.normalize()
df.sort_values(by=['AppID', 'Date'], inplace=True)

# Remove duplicate rows based on 'AppID' and 'Phase' columns, keeping the last occurrence of each row.
df.drop_duplicates(subset=['AppID', 'Phase'], keep='last', inplace=True)

# Filter the DataFrame to only include rows where 'Phase' is one of the allowed values.
allowed_values = ['General Availability', 'End of Support', 'End of Extended Support']
filter_df = df[df['Phase'].isin(allowed_values)]

# Pivot the DataFrame to create a new DataFrame with 'AppID' as the index and 'Phase' as the columns.
pivoted_df = filter_df.pivot(index='AppID', columns='Phase', values='Date')
pivoted_df.columns=['End of Extended Support', 'End of Support', 'General Availability']
pivoted_df = pivoted_df[['General Availability', 'End of Support', 'End of Extended Support']]

# Create a new DataFrame with 'AppID' and 'Name' columns from the original DataFrame.
dfapps = df[['AppID', 'Name']].copy()
dfapps.drop_duplicates(subset=['AppID'], keep='last', inplace=True)

# Merge the two DataFrames on 'AppID'.
dfapps = dfapps.set_index('AppID')
dfcombined = pd.merge(dfapps, pivoted_df, on='AppID', how='left')

# Apply the support_state function to each row of the DataFrame.
dfcombined['Support State'] = dfcombined.apply(support_state, axis=1)
dfcombined['General Availability'] = dfcombined['General Availability'].dt.strftime('%Y-%m-%d')
dfcombined['End of Support'] = dfcombined['End of Support'].dt.strftime('%Y-%m-%d')
dfcombined['End of Extended Support'] = dfcombined['End of Extended Support'].dt.strftime('%Y-%m-%d')
dfcombined.fillna('', inplace=True)

print(dfcombined)