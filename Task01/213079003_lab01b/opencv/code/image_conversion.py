# IMAGE CONVERSION
import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description= "Image Conversion")
parser.add_argument('path_to_image', nargs='+',type=str)
args = parser.parse_args()


img_path = str(args.path_to_image[0])

# reading an RGB image
bgr_img = cv2.imread(img_path)

# OpenCV reads an RGB image as BGR image. So we need to convert into RGB image
rgb_img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2RGB)

# storing the image pixels into a numpy array
pixels = np.asarray(rgb_img,dtype='uint8')

# normalized pixel array
pixels_normalized = pixels/np.max(pixels)

# plotting original and normalized images using matplotlib
fig = plt.figure(figsize=(7,7))
fig.add_subplot(1,2,1)
plt.imshow(pixels)
plt.title("Original Image",fontsize="12")

fig.add_subplot(1,2,2)
plt.imshow(pixels_normalized)
plt.title("Normalized Image",fontsize="12")
plt.savefig("../results/matplotlib_images.png") # saving the matplotlib images
plt.show()

# plotting original and normalized images using opencv

norm_Image = cv2.normalize(bgr_img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

cv2.imshow("Original Image",bgr_img)
cv2.imshow("Normalized Image",norm_Image)
# saving the opencv images
cv2.imwrite("../results/Original_opencv_img.png",bgr_img)
cv2.imwrite("../results/Normalized_opencv_img.png",norm_Image*255)

cv2.waitKey(0)
cv2.destroyAllWindows()
