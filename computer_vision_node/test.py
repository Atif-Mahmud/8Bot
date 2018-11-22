import numpy as np
import cv2
from calibrate import calibrate
from yaml_config import loadYAML 
from center_of_shape import contours 

cap = cv2.VideoCapture(1)

ret, frame = cap.read()

cv2.imshow("original frame", frame)

frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
transform = calibrate(frame, loadYAML('parameters.yml'))
cv2.waitKey()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(transform(frame), cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    contours(gray)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()