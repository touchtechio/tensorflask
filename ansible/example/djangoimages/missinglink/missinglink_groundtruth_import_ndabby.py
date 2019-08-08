import os, csv, datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "missinglink.settings")
import django
django.setup()

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from groundtruth.models import Image

path = './data/MissingLink_Groundtruth_PNG_NDabby.csv'
print(Image.objects.all())

time = timezone.now() + datetime.timedelta(days=-60)


def updateNDabbyImageData(update_image, row):

    asset = row['Asset Type']
    character = row['Character']
    pose = row['Face Pose']
    obstructed = row['Face Obstructed']

    # print once every hundred rows so we know something is happening
   # if (index % 100 == 0):
    if (asset is not ''):
        print(index, ':', row['ImageFilename'], row['ImageExtension'], asset, character, pose, obstructed)
        update_image.tags.add("asset-"+asset)
        update_image.tags.add("character-"+character)
        update_image.tags.add("pose-"+pose)
        update_image.tags.add("obstructed-"+obstructed)



update = 0
create = 0

with open(path) as csvfile:
    reader = csv.DictReader(csvfile)
    index = 0
    for row in reader:

        #if (index == 2000):
        #    break

        #csv values
        filename = row['ImageFilename']
        directory = row['ImageDirectory']
        extension = row['ImageExtension']

        asset = row['Asset Type']

        if (asset is not ''):

            try:
                update_image = Image.objects.get(filename=filename)

                updateNDabbyImageData(update_image, row)

                # update_image.tags.add('original-add')
                update_image.save()
                update += 1

            # insert a row
            ##self.cur.execute(
            ##    "INSERT INTO IMAGES (ID,FILENAME,PATH,EXT,TAGS) VALUES (" + str(index) + ", '" + row[
            ##        'ImageFilename'] + "', '" + row['ImageDirectory'] + "', '" + row['ImageExtension'] + "', 'original')")
            except ObjectDoesNotExist:
                #update_image = Image.objects.create(filename=filename, pub_date=time)
                #print("creating", filename)
                create += 1


        # print once every hundred rows so we know something is happening
        if (index % 100 == 0):
            print(index, ':', row['ImageFilename'], row['ImageExtension'], row['Character'])

        # commit each insertion
        ##self.commit()
        index += 1

    print(index, ' rows scanned!')
    print(create, ' images created!')
    print(update, ' records affected!')


