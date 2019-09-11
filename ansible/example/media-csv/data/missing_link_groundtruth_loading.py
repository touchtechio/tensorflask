# -*- coding: utf-8 -*-

import os
import csv

path = 'data/faces'


# TODO: neeeds main function,  arg parse, for path and destination csv
# TODO: other values from filesystem
# TODO: DIRECTORY and path standards
# TODO : logging
# user validate length with unix command :  find . | wc -l
# aws s3 cp "resume.pdf" s3://content.touchtech.io/MissingLink --metadata 'resume=yes' --dry-run
# cd /Volumes/Samsung_T5/MissingLink_Groundtruth_PNG/
# aws s3 cp 0600.0450.hanm.001_PNG/ s3://content.touchtech.io/MissingLink --metadata 'resume=yes' --recursive
#aws s3 sync 0600.0450_PNG/ s3://content.touchtech.io/tmp_more_MissingLink --metadata 'resume=yes'



#external path
src_folder_path = './MissingLink_Groundtruth_PNG'

## TODO: os.env('ROOTMEDIA')
dst_data_path = '~/dev/git/tensor/ansible/example/media-csv/data/data'



with open(dst_data_path + '/image-MissingLink_Groundtruth_PNG.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ImageFilename', 'ImageDirectory'])
    for dirpath, _, filenames in os.walk(src_folder_path):
        if filenames:
            for file in filenames:
                writer.writerow([file, dirpath])


