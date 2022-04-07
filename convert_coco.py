import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "G:/results2/"

# set path for coco json to be saved
save_json_path = "s/all_data2.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)