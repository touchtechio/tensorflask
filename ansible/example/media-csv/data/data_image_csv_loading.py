# -*- coding: utf-8 -*-

import csv

path = 'data/Laika-Kubo.csv'

with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(reader.line_num, ':', row['ImageFilename'])

# with open('/tmp/laika-files.csv', 'w', encoding='utf8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['ImageFilename', 'ImageDirectory'])
#     for dirpath, _, filenames in os.walk(path):
#         if filenames:
#             for file in filenames:
#                 writer.writerow([file, dirpath])


