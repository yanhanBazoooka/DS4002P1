import pandas as pd

# Load the uploaded Excel file to see its contents
file_path = 'Your/Path'
data = pd.read_excel(file_path)

# Load the second sheet (Sheet1) from the uploaded Excel file
sheet1_data = pd.read_excel(file_path, sheet_name='Sheet1')

# Rename the 'Published Date' column in the second dataset to 'Date' for consistency
sheet1_data_renamed = sheet1_data.rename(columns={'Published Date': 'Date'})

# Merge the two datasets on the 'Date' column
merged_data = pd.merge(data, sheet1_data_renamed, on='Date', how='outer')

# Sort the merged dataset by date
merged_data_sorted = merged_data.sort_values(by='Date')

# Remove rows where both 'NVDA' and 'LCID' column values are NaN
cleaned_data = merged_data_sorted.dropna(subset=['NVDA', 'LCID'], how='all')

# Save the cleaned dataset to a new Excel file
cleaned_file_path = '/Your/Path'
cleaned_data.to_excel(cleaned_file_path, index=False)

# Separate the dataset for NVDA, drop NaN in specified columns, and save to a new file
nvda_data = cleaned_data[['Date', 'NVDA_daily_percent', 'NVDA']].dropna(subset=['NVDA', 'NVDA_daily_percent'])
nvda_file_path = '/Your/Path'
nvda_data.to_excel(nvda_file_path, index=False)

# Separate the dataset for LCID, drop NaN in specified columns, and save to a new file
lcid_data = cleaned_data[['Date', 'LCID_daily_percent', 'LCID']].dropna(subset=['LCID', 'LCID_daily_percent'])
lcid_file_path = '/Your/Path'
lcid_data.to_excel(lcid_file_path, index=False)

