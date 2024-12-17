import csv

# Define the input and output file paths
input_file_path = '2023.txt'
output_file_path = '2023.csv'

with open(input_file_path, 'r') as txt_file, open(output_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    headers = ['Pitches', 'Zone%',	'Whiff%', 'WOBA']
    csv_writer.writerow(headers)

    for line in txt_file:
        line = line.replace(',', '')
        columns = line.strip().split()
        csv_writer.writerow(columns)