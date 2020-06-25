"""This module is used to create a new base dir having selected classes.

for example, if you have the IMAGES stored in the following directory 
structure(which is standard structure for most of the time).

images
    - train
        - cats
            - cat1.jpeg
            - cat2.png
            - cat3.jpg
            .
            .
            .
        - dogs
            - dog1.png
            - dog2.jpeg
            - dog3.jpg
            .
            .
            .
        - horses
            - horse1.png
            - horse2.jpeg
            - horse3.jpg
            .
            .
            .
    - test
        - cats
            - cat1.jpeg
            - cat2.png
            - cat3.jpg
            .
            .
            .
        - dogs
            - dog1.png
            - dog2.jpeg
            - dog3.jpg
            .
            .
            .
        - horses
            - horse1.png
            - horse2.jpeg
            - horse3.jpg
            .
            .
            .

Here images is the root/base dir, train dir and test dir are train and test sets, 
cats dir(having images of cats) and dogs dir(having images of dogs) are cat and dog class labels.

But suppose you want only dogs and cats and you don't want cats.

This module is going to help you achive this and all dataset having this kind of structure"""

def mkdir(p):
  if not os.path.exists(p):
    os.mkdir(p)

def link(src, dst):
  if not os.path.exists(dst):
    os.symlink(src, dst, target_is_directory=True)

mkdir('../large_files/fruits-360-small')


classes = [
  'Apple Golden 1',
  'Avocado',
  'Lemon',
  'Mango',
  'Kiwi',
  'Banana',
  'Strawberry',
  'Raspberry'
]

train_path_from = os.path.abspath('../large_files/fruits-360/Training')
valid_path_from = os.path.abspath('../large_files/fruits-360/Validation')

train_path_to = os.path.abspath('../large_files/fruits-360-small/Training')
valid_path_to = os.path.abspath('../large_files/fruits-360-small/Validation')

mkdir(train_path_to)
mkdir(valid_path_to)


for c in classes:
  link(train_path_from + '/' + c, train_path_to + '/' + c)
  link(valid_path_from + '/' + c, valid_path_to + '/' + c)


    




























