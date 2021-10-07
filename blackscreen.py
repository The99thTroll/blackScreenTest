import time
import numpy
import cv2

fourCC = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.avi", fourCC, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(4)

image = cv2.imread('ghirardelliSquare.jpeg')

for i in range(60):
    ret = cap.read()
    
while cap.isOpened():
    ret, frame = cap.read()
   
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
            
    lower_black = numpy.array([30, 30, 00])
    upper_black = numpy.array([104, 153, 70])
    
    mask_1 = cv2.inRange(frame, lower_black, upper_black)
    
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, numpy.ones((3, 3), numpy.uint8))
    
    res = cv2.bitwise_and(frame, frame, mask=mask_1)
    
    f = frame - res
    f = numpy.where(f == 0, image, f)

    cv2.imshow('Video', frame)
    cv2.imshow('Mask', f)
    cv2.waitKey(1)
        
cap.release()
output_file.release()
cv2.destroyAllWindows()