"""Work with CSV files in normal Python"""

import csv

with open('./original.csv') as file:
    reader_object = csv.reader(file, delimiter=";")
    all_rows = list(reader_object)

with open('./output.csv', 'w', newline='') as output:
    writer_object = csv.writer(output)
    for line in all_rows:
        writer_object.writerow(line)


# for id, name in all_rows:
#     print(id, name)
