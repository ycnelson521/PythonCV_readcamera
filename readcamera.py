import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #Capture fraem by frame
    ret, frame = cap.read()

    #convert to gray image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display the resulting frame
    cv2.imshow('color', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the capture
cap.release()
cv2.destroyAllWindows()


