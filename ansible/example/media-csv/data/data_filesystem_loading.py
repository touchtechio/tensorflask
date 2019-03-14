# -*- coding: utf-8 -*-

import os
import csv

path = '/Users/pinnermx/Pictures'
#path = '/duo/contentai/Laika Data_ 02202019/PKG - Kubo training data/Marketing_Kubo/'


def remove_path(text):
    if text.startswith(path):
        return text[len(path):]
    return text


def split_fileext(text):
    name = os.path.splitext(text)[0]
    ext = os.path.splitext(text)[1]
    return name, ext


with open('./Laika-Kubo.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ImageFilename', 'ImageDirectory', 'ImageExtension'])
    for dirpath, _, filenames in os.walk(path):

        dirpath = remove_path(dirpath)
        if filenames:
            for file in filenames:
                name, ext = split_fileext(file)
                print([name, dirpath, ext])

