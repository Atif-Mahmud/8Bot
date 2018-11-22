import numpy as np
import cv2
from calibrate2 import calibrate
from yaml_config import loadYAML 
from center_of_shape import contours 

cap = cv2.VideoCapture(1)

ret, frame = cap.read()

cv2.imshow("original frame", frame)
cv2.waitKey()

transform = calibrate(frame)
test = transform(frame)
contours(test)
cv2.waitKey()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    output = transform(frame)

    # Display the resulting frame
    contours(output)
    cv2.imshow('Live Feed',output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()