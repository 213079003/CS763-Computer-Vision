# DISPLAY VIDEO
import cv2
import argparse

parser = argparse.ArgumentParser(description= "Display Video")
parser.add_argument('--path', nargs='+',type=str)
args = parser.parse_args()

if args.path is not None:
    video_path = str(args.path[0])
    cap = cv2.VideoCapture(video_path)
else:
    cap = cv2.VideoCapture(0)

# Check if video captured successfully

if (cap.isOpened()== False):
    print("Error opening video stream or file")


while (cap.isOpened()):

    istrue, frame = cap.read()  

    font = cv2.FONT_HERSHEY_SIMPLEX
    winname = "Gray-scale video"
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.rectangle(frame,(492,15),(618,38),color = (255,255,225),thickness=-1)
    cv2.putText(frame, "SRINIDHI", (490,37), font, 1, (0,0,0), 1) 
    
    cv2.rectangle(frame_gray,(492,15),(618,38),color = (255,255,225),thickness=-1)
    cv2.putText(frame_gray, "SRINIDHI", (490,37), font, 1, (0,0,0), 1)  
    
    cv2.namedWindow('Original video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Original video', 640, 480)
    cv2.moveWindow('Original video', 150,175)
    cv2.imshow("Original video", frame)
    
    cv2.namedWindow(winname)
    cv2.moveWindow(winname, 791,174)    
    cv2.imshow(winname,frame_gray)
    if cv2.waitKey(20) & 0xFF==ord('q'): # if we press q, the video window gets closed
             break
cap.release()
cv2.destroyAllWindows()


