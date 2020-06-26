from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

IMG_PATH = "/content/fruits-360-small/Training/Raspberry/116_100.jpg"

img = image.load_img(IMG_PATH, target_size=(224, 224))
plt.imshow(img)