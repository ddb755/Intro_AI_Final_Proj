# -*- coding: utf-8 -*-
"""Balsara_final_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WRVotp67CwNUkXlFDuoCo2WKukVIPuLK
"""

!pip install numpy scikit-learn

import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from PIL import Image
from IPython.display import display

"""Load Images into Co-Lab"""

#function used to download images from data folder
def load_data(image_path):
  img=Image.open(image_path)
  #change image size for faster processing
  img=img.resize((200,200))
  return np.array(img)

def load_images(folder):
  images=[]

  for filename in os.listdir(folder):
    image_path=os.path.join(folder, filename)
    image=cv2.imread(image_path)
    if image is not None:
      images.append(image)
  return images

images=[]
data_path='./' #path from co lab

for file in os.listdir(data_path):
  #only jpgs will be uploaded
  image_path= os.path.join(data_path, file)
  image= load_data(image_path)
  images.append(image)

display(images[0])
loaded_data=load_data(data_path)

def flatten_image(image):
  return image.reshape((-1, image.shape[-1]))
  #flatten 3D array representing image (width, height, RGB channels into 2D array (pixels x RGB channels))
  #information for this code found at https://www.geeksforgeeks.org/impact-of-image-flattening/

def kmeans_clustering(images,n_clusters=5):
  kmeans_test=KMeans(n_clusters=n_clusters, random_state=56)
  kmeans_test.fit(images)
  return kmeans_test.cluster_centers_.astype(int)

def display_colors(centers):
  plt.figure(figsize=(10,2))
  for color in centers:
    color_cluster=np.zeros((50,50,3), dtype=np.uint8)