import cv2
import time
import numpy as np

#Starting the webcam
cap = cv2.VideoCapture(0)

image = cv2.imread("me.jpeg")


#Reading the captured frame until the camera is open
while True:
    ret, img = cap.read()
    img = cv2.resize(img,(640,480))
    image = cv2.resize(image,(640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask = cv2.inRange(img,l_black,u_black)
    res = cv2.bitwise_and(img,img,mask = mask)

    f = img - res
    f = np.where(f ==0, image, f) 

    #Displaying the output to the user
    cv2.imshow("video", img)
    cv2.imshow("mask", f)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break



cap.release()
cv2.destroyAllWindows()
