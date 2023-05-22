================================ CS764 Lab 01b ================================

1. Screen Name : SRINIDHI

2. Which external person (human resource) other than group members or TA I consulted:  None

3. What resources I used on the Internet:  (List of URLs)

	  a. https://docs.python.org/3/howto/argparse.html

	  b. https://numpy.org/doc/stable/user/quickstart.html

	  c. https://numpy.org/doc/stable/reference/routines.array-manipulation.html

	  d. https://www.javatpoint.com/k-means-clustering-algorithm-in-machine-learning

	  e. https://medium.com/machine-learning-algorithms-from-scratch/k-means-clustering-from-scratch-in-python-1675d38eee42

	  f. https://docs.opencv.org/3.4.2/dc/d2e/tutorial_py_image_display.html

	  g. https://docs.opencv.org/3.4.2/dd/d43/tutorial_py_video_display.html

	  h. https://stackoverflow.com/questions/56270389/how-to-wait-for-two-different-keys-using-cv2-waitkey

	  i. https://matplotlib.org/stable/tutorials/introductory/pyplot.html


4. Honor Code
I pledge on my honour (Bhagwat Gita) that I have not given or received any unauthorized assistance on this assignment or any previous task.  
	Signed by:  Srinidhi

5. Since this is an individual assignment. I am the only contributor.
Questions | Me  | Roll Number

a. Python | 100 | 213079003

b. Numpy  | 100 | 213079003

c. OpenCV | 100 | 213079003

 Instructions to run:

  1) P- norm
     The python file p_norm.py is in the path ../python/code/
     - An example with p=3 and a vector (2.3,21,4,1) is shown below
        ```
        python p_norm.py 2.3 21 4 1 --p 3
        ```
     The following instruction should be used if p=2 is required
      ```
	    python p_norm.py 2.3 21 4 1
      ```
--------------------
  2) Row Manipulation
     The python file row_manipulation.py is in the path ../numpy/code/ 
     - An example with N=4 is shown below
      ```
	    python row_manipulation.py --N 4
      ```
--------------------
  3) k-Means Clustering algorithm
     The python file kmeans.py is in the path ../numpy/code/ 
     - Run the following command
      ```
	    python kmeans.py
      ```
    This python file forms k-clusters and displays the input sample points and 
	 output image having k-clusters.
--------------------
  4) Image Conversion
     The python file image_conversion.py is in the path ../opencv/code/ 
     Run the following command specifying the path of image inplace of
	 path_to_image
	 (The image "image.png" in "../opencv/data/" directory can be used)
      ```
	    python image_conversion.py path_to_image
      ```
     When the program runs, it opens a window showing the images displayed using 
	 matplotlib module.The window can be closed either by pressing the close button
	 ('x' button) of the window or pressing 'q' in keyboard. After closing the window,
	 another two windows will popup displaying the images using opencv module. 
     These windows can also be closed in the same way.
--------------------
  5) Display Images
     - This python file presents a slideshow of images(display00.png to display05.png images) 
	 in "../opencv/data/" directory. 
     - The python file display_images.py is in the path ../opencv/code/ 
     - Run the following command (data is the folder containing the images to be displayed)
      ```
	    python display_images.py data
      ```
     - When the program runs, it initially displays "display00.png" image window. 
     - Pressing key 'n' displays the next image and pressing key 'p' displays the previous image. 
     - The image window can be closed by pressing the close button('x' button) of the window.
--------------------
  6) Display Video
     - The python file display_video.py is in the path ../opencv/code/ 
	 
     - Run the following command specifying the path of video inplace of
	   path_to_video_file
	  (The video file "sample_video.mp4" in "./opencv/data/" directory can be used)
	    ```    
	    python display_video.py --path path_to_video_file
	    ``` 
	 - Run the following command if webcam is to be used
      ```	 
	    python display_video.py 
	    ``` 
     - This python file displays orginal and gray-scale version of a video (side-by-side) 
	 annoted with text. Pressing key 'q' closes the windows.
---------------------------------
