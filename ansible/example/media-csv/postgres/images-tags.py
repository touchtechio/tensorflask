import images as im

#generate csv from filesystem
#i used ../data/data_laika_loading.py

# open database connction
image_table = im.Images()

#get all images
#images = image_table.get_all()

#get all with a substring
# something like this sql = "SELECT * FROM IMAGES where TAGS LIKE '%" + tag + "%'"
images = image_table.get_all_by_tag("test")

for name, row in images.iterrows():
    print(row['filename'], row['tags'])

