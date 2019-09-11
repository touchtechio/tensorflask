import images as im
import random
import csv


#generate csv from filesystem
#i used ../data/data_missing_link_groundtruth_loading.py
IMAGE_CSV = '../data/data/MissingLink_Groundtruth_PNG.csv'

# open database connction
image_table = im.Images(db_location="127.0.0.1", db_port=63333)

# blow away entire db and rebuild from ../data/data/Laika-Kubo.csv
def refresh_images():
    # drop teh images table
    image_table.drop_table()
    # create a images table from scratch
    image_table.create_table()

    # fill the images table from csv
    image_table.fill_table(path=IMAGE_CSV)
#

    # save your work
    image_table.commit()


def add_tag(file, tag):
    image = None
    if isinstance(file, (int)):
        image = image_table.get_by_index(file)
    else:
        image = image_table.get_by_name(file)

    current_tags = image['tags'].values[0]
    if tag not in current_tags:
        tag = current_tags + " " + tag
        image_table.execute(
            "UPDATE IMAGES set tags = '"+tag+"' where id = " + str(image['id'].values[0]) + ";")
        image_table.commit()


def add_frameno(file, frameNo):
    image = None
    if isinstance(file, (int)):
        image = image_table.get_by_index(file)
    else:
        image = image_table.get_by_name(file)

    image_table.execute("UPDATE IMAGES set frame_no = "+frameNo+" where id = " + str(image['id'].values[0]) + ";")
    image_table.commit()


def add_scene_shot_frame_no(file, scene_no, shot_no, frame_no):

    if scene_no is None or shot_no is None or frame_no is None:
        print("error: skipping file with no scene, shot, or frame : " + file)
        return

    if isinstance(file, (int)):
        image = image_table.get_by_index(file)
    else:
        image = image_table.get_by_name(file)

    image_table.execute("UPDATE IMAGES set"
                        + " scene_no = " + scene_no + ","
                        + " shot_no = " + shot_no + ","
                        + " frame_no = " + frame_no
                        + " where id = " + str(image['id'].values[0]) + ";")
    image_table.commit()


def print_panda(panda):
    print('SHAPE:     ', images.shape)
    print('DIMENSIONS:', images.ndim)
    print('DATA TYPES:\n', images.dtypes)
    print('INDEXES:   ', images.index)
    print('HEAD:      \n', images.head())


def write_result_groundtruth(images):
    # run the full data set
    # verrrry slow, if you are writting
    #for name, row in images[1:20].iterrows():

    for name, row in images.iterrows():
        #  print(name)
        #  print(row)
        # print(row['filename'].split('.')[-1])

        id = row['id']

        pnt = row['filename'].split('.')[2]
        if pnt == "pnt":
            add_tag(id, "groundtruth-result")

            intel_nodes_renders = row['filename'].split('.')[3]
            if intel_nodes_renders == "intel_nodes_renders":
                add_tag(id, "groundtruth-mask")

            if "out_sr_sideburn_holdout" in row['filename']:
                add_tag(id, "out_sr_sideburn_holdout")

            if "out_sl_sideburn_holdout" in row['filename']:
                add_tag(id, "out_sl_sideburn_holdout")

            if "out_sr_eye" in row['filename']:
                add_tag(id, "out_sr_eye")

            if "out_sl_eye" in row['filename']:
                add_tag(id, "out_sl_eye")

            if "out_sr_eyebrow" in row['filename']:
                add_tag(id, "out_sl_eyebrow")

            if "out_sr_eyebrow" in row['filename']:
                add_tag(id, "out_sl_eyebrow")
        else:
            add_tag(id, "groundtruth-source")



def write_shot_no(images):
    # run the full data set
    # verrrry slow, if you are writting
    #for name, row in images[1:20].iterrows():

    for name, row in images.iterrows():
        #  print(name)
        #  print(row)
        # print(row['filename'].split('.')[-1])

        id = row['id']

        ## ADD FRAME NO
        frameNo = row['filename'].split('.')[-1]
        frameNoTag = "frameNo-" + frameNo

        ## ADD SHOT NO
        shotNo = row['filename'].split('.')[1]
        shotNoTag = "shotNo-" + shotNo

        ## ADD SCENE NO
        sceneNo = row['filename'].split('.')[0]
        sceneNoTag = "sceneNo-" + sceneNo

        print(row['filename'], "shot:", shotNoTag, "scene:", sceneNoTag)

        if frameNo is None or shotNo is None or sceneNo is None:
            print("error: skipping file with no scene, shot, or frame : " + name)

        else:
            add_scene_shot_frame_no(id, sceneNo, shotNo, frameNo)

          # write tag
          #add_tag(id, shotNoTag)
          #   add_tag(id, sceneNoTag)
          #   add_tag(id, frameNoTag)



        ## ADD CAMERA LEFT OR RIGHT OR D
        # frameNo = row['filename'].split('.')[-2]
        # print(row['filename'].split('.')[-2])
        cameraTag = "camera-" + row['filename'].split('.')[-2]

        # write left/right camera
        add_tag(id, cameraTag)






## use this to load fresh data from csv
refresh_images()

#image_table.execute("SELECT * from IMAGES where TAGS like '*tgilch*';")

# get all from the postgres db into a panda
images = image_table.get_all()

# try looking at it again
print_panda(images)


#print(images)
# look at stuff
for name, row in images[1:20].iterrows():
  #  print(name)
  #  print(row)
    print(row['id'], row['filename'], row['tags'], row['ext'])
  #  row['TAGS'] = 'character'



# crunch through everything
# parse filenames and make tags
# populate the frame_no
# test like this with a limited set


write_shot_no(images)

write_result_groundtruth(images)

#  row['TAGS'] = 'character'



#
# for name, row in images[1].iterrows():
#     print(name)
#     print(row)
#     print(row['filename'], row['tags'], row['ext'])
#
#     frameNumber = row['filename'].split(".")[:-1]
#     print("frameNumber:" + frameNumber)
#   #  row['TAGS'] = 'character'
#



#
# image = image_table.get_by_index(1)
# print(image)
#
# image = image_table.get_by_name('0400.1000.final.sireland.0002.0043.exr')
# print(image)
# print(image['tags'].values)
#
# # make a random tag and add it
# random_int = random.randint(10, 100)
# random_tag = 'test-tag-' + str(random_int)
# add_tag('0400.0697.final.mbeightol.0001.0042', random_tag)
# add_tag('0400.0697.final.mbeightol.0001.0042', random_tag)
# add_tag(random_int, random_tag)
#
#
# print("CHECK RECORD FOR TAG: ", random_tag)
# image = image_table.get_by_name('0400.0697.final.mbeightol.0001.0042')
# print(image)
# print(image['tags'].values)
#
#
# print("SEARCH FOR TAG: ", random_tag)
# image = image_table.get_all_by_tag(random_tag)
# print(image)
# print(image['tags'].values)

# image_table.execute("UPDATE IMAGES set TAGS = 'character' where FILENAME = '0400.1000.final.sireland.0002.0043.exr';")
# image_table.commit()
#
# images = image_table.get_all()
# for name, row in images[1:10].iterrows():
#     # print(name)
#     # print(row)
#     print(row['FILENAME'], row['TAGS'])
#   #  row['TAGS'] = 'character'
#
#
# # image_table.update(images)
# # image_table.commit()
#
#
# images.to_csv("/tmp/panda-export.csv")