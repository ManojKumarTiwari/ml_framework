import tensorflow as tf
from tensorflow import keras
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

def classify(img_path):
  """This funntion classifies any given image.
  Note: it used pretrained vgg16 on imagenet"""
  # load the image
  img = image.load_img(img_path, target_size=(224, 224))
  # load the model
  model = VGG16()
  # conver the image to array
  img_array = image.img_to_array(img)
  # add the batch dimension as all deep learning models expects input shape of (batch, height, width, channel)
  img_batch = np.expand_dims(img_array, axis=0)
  # preprocess
  img_processed = preprocess_input(img_batch)
  # predict
  prediction = model.predict(img_processed)
  # decode predictions
  print(decode_predictions(prediction))
  #print(prediction)