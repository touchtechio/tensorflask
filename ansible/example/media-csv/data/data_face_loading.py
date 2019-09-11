# -*- coding: utf-8 -*-

import os
import csv

path = 'data/faces'


# TODO: neeeds main function,  arg parse, for path and destination csv
# TODO: other values from filesystem
# TODO: DIRECTORY and path standards
# TODO : logging

#external path
path = '/Volumes/Samsung_T5/MissingLink_Groundtruth_PNG'

with open('/tmp/image-MissingLink_Groundtruth_PNG.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ImageFilename', 'ImageDirectory'])
    for dirpath, _, filenames in os.walk(path):
        if filenames:
            for file in filenames:
                writer.writerow([file, dirpath])


