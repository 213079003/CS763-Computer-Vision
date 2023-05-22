# DISPLAY IMAGES
import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(description= "Slideshow of Images")
parser.add_argument('path_to_directory_containing_images', nargs='+',type=str)
args = parser.parse_args()


imgs_path = "../" + str(args.path_to_directory_containing_images[0])
images = os.listdir(imgs_path)
l =[]
for i in images:
    if str(i) != "image.png" and str(i)!= "sample_video.mp4":
        img = cv2.imread(os.path.join(imgs_path,str(i)))
        l.append(list(img))

i=0

def next_img(i):
    i = (i+1) % len(l)
    current_img(i)

def previous_img(i):
    i = (i-1) % len(l)
    current_img(i)

def current_img(i):
    cv2.imshow("Img",np.asarray(l[i]))
    pressedKey = cv2.waitKey(0) & 0xFF  

    if pressedKey == ord('n'): 
        next_img(i)
    elif pressedKey == ord('p'):
        previous_img(i) 
    else:        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
              
current_img(i)

