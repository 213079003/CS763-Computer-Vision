# -*- coding: utf-8 -*-
"""CV_Task06_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DCGGkEap0Tq4P68tAi-6wXGcrNx8x4ya
"""

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

stable_filenames = sorted(os.listdir('/content/drive/MyDrive/Academics/Semester 2/Computer Vision/DeepStab/DeepStab/stable'), key = lambda x: int(x.split('.avi')[0]))
unstable_filenames = sorted(os.listdir('/content/drive/MyDrive/Academics/Semester 2/Computer Vision/DeepStab/DeepStab/unstable'), key = lambda x: int(x.split('.avi')[0]))

path = os.path.join("/content/drive/MyDrive/Academics/Semester 2/Computer Vision/DeepStab/DeepStab/unstable", unstable_filenames[0])

video_cap = cv2.VideoCapture(path)

def data_loader_train(path, unstable_filenames, stable_filenames):
    idx = np.random.randint(0,61)

    print("Data point loaded : ", idx)
    unstable_video_file = unstable_filenames[idx]
    stable_video_file = stable_filenames[idx]

    stable_frames = []
    unstable_frames = []

    path_1 = os.path.join(path + "/unstable", unstable_video_file)
    path_2 = os.path.join(path + "/stable", stable_video_file)

    unstable_cap = cv2.VideoCapture(path_1)
    stable_cap = cv2.VideoCapture(path_2)

    # Getting the number of frames
    if(unstable_cap.get(7) == stable_cap.get(7)):
      nf = unstable_cap.get(7)
    else:
      print("Error : frame counts don't match")

    # Getting a random frame
    id_frame = np.random.randint(0,nf)

    unstable_cap.set(cv2.CAP_PROP_POS_FRAMES, id_frame)
    stable_cap.set(cv2.CAP_PROP_POS_FRAMES, id_frame)

    ret, frame_0 = unstable_cap.read()
    if ret:
      uns_frame_0 = cv2.resize(frame_0, (256,256))
    else:
      print(1)
      print("Error in capturing frame")

    unstable_cap.set(cv2.CAP_PROP_POS_FRAMES, id_frame + 1)
    stable_cap.set(cv2.CAP_PROP_POS_FRAMES, id_frame + 1)

    ret, frame_1 = unstable_cap.read()
    if ret:
      uns_frame_1 = cv2.resize(frame_1, (256,256))
    else:
      print(2)
      print("Error in capturing frame")

    ret, frame_1= stable_cap.read()
    if ret:
      s_frame_1 = cv2.resize(frame_1, (256, 256))
    else:
      print(3)
      print("Error in capturing frame")

    if ret:
      x = np.stack([uns_frame_0, uns_frame_1], axis=0)
      y = s_frame_1
    else:
      print("Error")
      x = 0;
      y = 0;
    return idx,x,y

idx,x,y = data_loader_train("/content/drive/MyDrive/Academics/Semester 2/Computer Vision/DeepStab/DeepStab", unstable_filenames, stable_filenames)

# Visualizing the frames
plt.imshow(y)

"""# Creating the network"""

import tensorflow as tf

tf.keras.backend.clear_session()

input_1 = tf.keras.layers.Input(shape = [256,256,3])
input_2 = tf.keras.layers.Input(shape = [256,256,3])

# Left arm of y_Net
x_l1 = tf.keras.layers.Conv2D(filters = 256, kernel_size=5, padding='same', activation='relu', name = 'left_layer_1')(input_1)
ds_l1 = tf.keras.layers.MaxPool2D(pool_size=2)(x_l1)

x_l2 = tf.keras.layers.Conv2D(filters = 128 , kernel_size=5, padding='same', activation='relu', name = 'left_layer_2')(ds_l1)
ds_l2 = tf.keras.layers.MaxPool2D(pool_size=2)(x_l2)

x_l3 = tf.keras.layers.Conv2D(filters = 64, kernel_size=5, padding='same', activation='relu', name = 'left_layer_3')(ds_l2)
ds_l3 = tf.keras.layers.MaxPool2D(pool_size=2)(x_l3) 


# Right arm of y-net
x_r1 = tf.keras.layers.Conv2D(filters = 256, kernel_size=5, padding='same', activation='relu', name = 'right_layer_1')(input_2)
ds_r1 = tf.keras.layers.MaxPool2D(pool_size=2)(x_r1)

x_r2 = tf.keras.layers.Conv2D(filters = 128 , kernel_size=5, padding='same', activation='relu', name = 'right_layer_2')(ds_r1)
ds_r2 = tf.keras.layers.MaxPool2D(pool_size=2)(x_r2)

x_r3 = tf.keras.layers.Conv2D(filters = 64, kernel_size=5, padding='same', activation='relu', name = 'right_layer_3')(ds_r2)
ds_r3 = tf.keras.layers.MaxPool2D(pool_size=2)(x_r3) 

# Concatenating both the left and right sides

concat_1 = tf.concat([ds_r3, ds_l3], axis=3)

central_2 = tf.keras.layers.Conv2D(filters = 64, kernel_size=5, padding='same', activation='relu', name = 'c_layer_1')(concat_1)
upsampling_2 = tf.keras.layers.UpSampling2D((2,2))(central_2)
central_3 = tf.keras.layers.Conv2D(filters = 128, kernel_size=5, padding='same', activation='relu', name = 'c_layer_2')(upsampling_2)
upsampling_3 = tf.keras.layers.UpSampling2D((2,2))(central_3)
central_4 = tf.keras.layers.Conv2D(filters = 128, kernel_size=5, padding='same', name = 'c_layer_3')(upsampling_3)
upsampling_4 = tf.keras.layers.UpSampling2D((2,2))(central_4)

output = tf.keras.layers.Conv2D(filters = 3, kernel_size =5, padding='same', activation='sigmoid', name = 'output')(upsampling_4)

model = tf.keras.Model(inputs = [input_1, input_2], outputs = output)

model.summary()

optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)
# Instantiate a loss function
loss_fn = tf.keras.losses.MeanSquaredError()

model.compile(optimizer=optimizer,
              loss=loss_fn,
              metrics=['accuracy'])

tf.keras.utils.plot_model(model, show_shapes=True)

epochs = 10000
loss_array = []
error_array = []
for i in range(epochs):
  try:
    idx,x,y = data_loader_train("/content/drive/MyDrive/Academics/Semester 2/Computer Vision/DeepStab/DeepStab", unstable_filenames, stable_filenames)
    # x[0] = np.reshape(x[0], (1,256,256,3))
    # x[1] = np.reshape(x[1], (1,256,256,3))
    x = np.reshape(x, (2,1,256,256,3))
    y = np.reshape(y, (1,256,256,3))
    with tf.GradientTape() as tape:
      y_predicted = model([x[0],x[1]], training=True)
      print(np.shape(y_predicted))
      print(np.shape(y))
      mse = tf.keras.losses.MeanSquaredError()
      loss = mse(np.uint8(255*y), y_predicted)
      loss_array.append(float(loss))
    grads = tape.gradient(loss, model.trainable_weights)
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    print("Training loss (for one batch) at step %d: %.4f"% (i, float(loss)))
  except:
    # error_array.append(idx)
    pass

plt.plot(loss_array)