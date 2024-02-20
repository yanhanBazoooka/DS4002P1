import re
from datetime import datetime

# Function to extract date from URL
def extract_date_from_url(url):
    # Regular expression to find date pattern (YYYY/MM/DD) in the URL
    match = re.search(r'/(\d{4}/\d{2}/\d{2})/', url)
    if match:
        # Extract the date string found in the URL
        date_str = match.group(1)
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        return date_obj
    else:
        # Return None if no date pattern is found
        return None

# Applying the function to the "Link" column to update the "Published Date" column
df['Published Date'] = df['Link'].apply(extract_date_from_url)

