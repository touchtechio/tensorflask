import images as im
import random

#generate csv from filesystem
#i used ../data/data_laika_loading.py

# open database connction
image_table = im.Images()

# blow away entire db and rebuild from ../data/data/Laika-Kubo.csv
def refresh_images():
    # drop teh images table
    image_table.drop_table()
    # create a images table from scratch
    image_table.create_table()
    # fill the images table from csv
    image_table.fill_table()
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


def print_panda(panda):
    print('SHAPE:     ', images.shape)
    print('DIMENSIONS:', images.ndim)
    print('DATA TYPES:\n', images.dtypes)
    print('INDEXES:   ', images.index)
    print('HEAD:      \n', images.head())




#refresh_images()

#image_table.execute("SELECT * from IMAGES where TAGS like '*tgilch*';")


images = image_table.get_all()

print_panda(images)



#print(images)


for name, row in images[1:10].iterrows():
    print(name)
    print(row)
    print(row['filename'], row['tags'], row['ext'])
  #  row['TAGS'] = 'character'




image = image_table.get_by_index(1)
print(image)

image = image_table.get_by_name('0400.1000.final.sireland.0002.0043.exr')
print(image)
print(image['tags'].values)

# make a random tag and add it
random_int = random.randint(10, 100)
random_tag = 'test-tag-' + str(random_int)
add_tag('0400.0697.final.mbeightol.0001.0042', random_tag)
add_tag('0400.0697.final.mbeightol.0001.0042', random_tag)
add_tag(random_int, random_tag)


print("CHECK RECORD FOR TAG: ", random_tag)
image = image_table.get_by_name('0400.0697.final.mbeightol.0001.0042')
print(image)
print(image['tags'].values)


print("SEARCH FOR TAG: ", random_tag)
image = image_table.get_all_by_tag(random_tag)
print(image)
print(image['tags'].values)

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