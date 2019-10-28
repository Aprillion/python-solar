"""Work with CSV files in normal Python"""

import csv

with open('./original.csv') as f:
    data = csv.reader()
    print(data)
