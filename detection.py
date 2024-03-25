import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture('../PBLM_project/vid.mp4')


# Check if the video capture object is opened successfully
if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

min_width_react = 80 #min width rectangle
min_height_react = 80

count_line_position= 400   
#Initialize substructor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()        

def center_point(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx= x+x1
    cy= y+y1
    return cx,cy

#list
detect = []
offset=6 #pixel error
counter=0


while True:
    ret, frame1 = cap.read()
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    #each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5,5), np.uint8))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    counterShape,h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1,(100,count_line_position),(550,count_line_position),(255,127,0),3)

    

    # Check if frame is read correctly
    if not ret:
        print("Error: Unable to read frame.")
        break

    for (i,c) in enumerate(counterShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w>= min_width_react) and (h>= min_height_react)
        if not validate_counter:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),2)

        center= center_point(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1,center,2,(0,0,255),-1)


        for (x,y) in detect:
            if y<(count_line_position+offset) and y>(count_line_position+offset):
                counter+=1
            cv2.line(frame1,(100,count_line_position),(550,count_line_position),(0,127,255),3)
            detect.remove((x,y))   
            print("Vehicle Counter:"+str(counter))

    cv2.putText(frame1,"Vehicle Counter :"+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)         

    cv2.imshow('Video Original',frame1)

    # Break the loop if 'Enter' key is pressed
    if cv2.waitKey(1) == 13:
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()

