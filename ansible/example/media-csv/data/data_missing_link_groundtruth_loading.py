# -*- coding: utf-8 -*-

import os
import csv



# TODO: neeeds main function,  arg parse, for path and destination csv
# TODO: other values from filesystem
# TODO: DIRECTORY and path standards
# TODO : logging
# user validate length with unix command :  find . | wc -l
# aws s3 cp "resume.pdf" s3://content.touchtech.io/MissingLink --metadata 'resume=yes' --dry-run
# cd /Volumes/Samsung_T5/MissingLink_Groundtruth_PNG/
# aws s3 cp 0600.0450.hanm.001_PNG/ s3://content.touchtech.io/MissingLink --metadata 'resume=yes' --recursive
#aws s3 sync 0600.0450_PNG/ s3://content.touchtech.io/tmp_more_MissingLink --metadata 'resume=yes'


path = '/Volumes/Samsung_T5/Kubo'
path = '/duo/contentai/Laika Data_ 02202019/PKG - Kubo training data/Marketing_Kubo/'
path = '/Volumes/Samsung_T5/MissingLink_Groundtruth_PNG'

def remove_path(text):
    if text.startswith(path):
        return text[len(path):]
    return text

def split_fileext(text):
    name = os.path.splitext(text)[0]
    ext = os.path.splitext(text)[1]
    return name, ext

with open('./data/MissingLink_Groundtruth_PNG.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ImageFilename', 'ImageDirectory', 'ImageExtension'])
    for dirpath, _, filenames in os.walk(path):

        dirpath = remove_path(dirpath)
        if "DStore" in dirpath:
            continue
        if filenames:
            for file in filenames:
                name, ext = split_fileext(file)
#                print([name, dirpath, ext])
                if "DS_Store" in name:
                    continue
                if "DS_Store" in ext:
                    continue
                writer.writerow([name, dirpath, ext])


