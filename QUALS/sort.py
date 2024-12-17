import os
import pandas as pd

# Define the directory containing the CSV files
directory = 'D:\coding\python\SABR\QUALS\csvs'

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Separate the data (example: split into two dataframes based on a condition)
        df1 = df[df['Lg'] == "AL"]
        df2 = df[df['Lg'] == "NL"]
        
        # Save the separated data to new CSV files
        df1.to_csv(os.path.join(directory, f'separated_{filename}_part1.csv'), index=False)
        df2.to_csv(os.path.join(directory, f'separated_{filename}_part2.csv'), index=False)
        # Append the separated data to two large CSV files
        output_file1 = os.path.join(directory, 'AL.csv')
        output_file2 = os.path.join(directory, 'NL.csv')

        # Append df1 to combined_part1.csv
        if not os.path.isfile(output_file1):
            df1.to_csv(output_file1, index=False)
        else:
            df1.to_csv(output_file1, mode='a', header=False, index=False)

        # Append df2 to combined_part2.csv
        if not os.path.isfile(output_file2):
            df2.to_csv(output_file2, index=False)
        else:
            df2.to_csv(output_file2, mode='a', header=False, index=False)