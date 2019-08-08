import os, csv, datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "missinglink.settings")
import django
django.setup()

from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from groundtruth.models import Image

path = './data/MissingLink_Groundtruth_PNG.csv'
print(Image.objects.all())

time = timezone.now() + datetime.timedelta(days=-60)


def updateImageSceneShotFrame(update_image):
    filename = update_image.filename

    frameNo = filename.split('.')[-1]

    ## ADD SHOT NO
    shotNo = filename.split('.')[1]

    ## ADD SCENE NO
    sceneNo = filename.split('.')[0]

    update_image.scene_no = sceneNo
    update_image.shot_no = shotNo
    update_image.frame_no = frameNo

    print(filename, " shot:", shotNo, " scene:", sceneNo, " frame:", frameNo)


def updateImageMaskTags(update_image):


    filename = update_image.filename

    cameraTag = "camera-" + filename.split('.')[-2]
    update_image.tags.add(cameraTag)

    # update_image.tags.add('original-add')

    pnt = filename.split('.')[2]
    if pnt == "pnt":
        update_image.tags.add("groundtruth-result")

        intel_nodes_renders = filename.split('.')[3]
        if intel_nodes_renders == "intel_nodes_renders":
            update_image.tags.add("groundtruth-mask")

        if "out_sr_sideburn_holdout" in filename:
            update_image.tags.add("out_sr_sideburn_holdout")

        if "out_sl_sideburn_holdout" in filename:
            update_image.tags.add("out_sl_sideburn_holdout")

        if "out_jaw_seam" in filename:
            update_image.tags.add("out_jaw_seam")

        if "out_sr_eye" in filename:
            update_image.tags.add("out_sr_eye")

        if "out_sl_eye" in filename:
            update_image.tags.add("out_sl_eye")

        if "out_sr_eyebrow" in filename:
            update_image.tags.add("out_sl_eyebrow")

        if "out_sr_eyebrow" in filename:
            update_image.tags.add("out_sl_eyebrow")

        if "out_jaw_seam" in filename:
            update_image.tags.add("out_jaw_seam")

        if "out_sl_bot_lid" in filename:
            update_image.tags.add("out_sl_bot_lid")

        if "out_sr_bot_lid" in filename:
            update_image.tags.add("out_sr_bot_lid")



    else:
        update_image.tags.add("groundtruth-source")



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

        try:
            update_image = Image.objects.get(filename=filename)

        except ObjectDoesNotExist:
            update_image = Image.objects.create(filename=filename, pub_date=time)
            #print("creating", filename)
            create += 1

        update_image.directory = row['ImageDirectory']
        update_image.extension = row['ImageExtension']

        updateImageSceneShotFrame(update_image)

        updateImageMaskTags(update_image)

        # update_image.tags.add('original-add')
        update_image.save()
        update += 1

        # insert a row
        ##self.cur.execute(
        ##    "INSERT INTO IMAGES (ID,FILENAME,PATH,EXT,TAGS) VALUES (" + str(index) + ", '" + row[
        ##        'ImageFilename'] + "', '" + row['ImageDirectory'] + "', '" + row['ImageExtension'] + "', 'original')")



        # print once every hundred rows so we know something is happening
        if (index % 1000 == 0):
            print(index, ':', row['ImageFilename'], row['ImageExtension'])

        # commit each insertion
        ##self.commit()
        index += 1

    print(index, ' rows scanned!')
    print(create, ' images created!')
    print(update, ' records affected!')


