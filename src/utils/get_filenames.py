from glob import glob
# useful for getting number of files
image_files = glob(TRAIN_PATH + '/*/*.jp*g')
valid_image_files = glob(VALIDATION_PATH + '/*/*.jp*g')