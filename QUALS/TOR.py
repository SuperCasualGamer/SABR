import pandas as pd

# Read the CSV file
df = pd.read_csv('AL.csv')

# Filter rows where the 'Tm' column contains 'TOR'
tor_df = df[df['Tm'] == 'TOR']

# Save the filtered rows to a new CSV file
tor_df.to_csv('TOR.csv', index=False)