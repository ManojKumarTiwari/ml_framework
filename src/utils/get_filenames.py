from glob import glob
# useful for getting number of files

TRAIN_PATH = ""
VALIDATION_PATH = ""

image_files = glob(TRAIN_PATH + '/*/*.jp*g')
valid_image_files = glob(VALIDATION_PATH + '/*/*.jp*g')

print(image_files)
print(valid_image_files)