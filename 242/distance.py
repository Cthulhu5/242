import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    cv2.circle(img, (320,240), 2, (0, 0, 255), 3);
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.blur(gray,(3,3))
    ret, binary = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
    (_,contours,hierarchy) = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    n=len(contours) 
    contoursImg=[]
    area = 0
    index = 0
    for i in range(n):
        if(cv2.contourArea(contours[i]) > area):
            area = cv2.contourArea(contours[i])
            index = i
    for i in range(n):
        M= cv2.moments(contours[index])
        cx = 0
        cy = 0
        if(M['m00'] != 0):
          cx = int(M['m10']/M['m00'])
          cy = int(M['m01']/M['m00'])
          text1 = "X:"+(str(cx-320));
          text2 = "Y:"+(str(cy-240));
          cv2.putText(img, text1, (200,280), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, 8)
          cv2.putText(img, text2, (200,320), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, 8)
          cv2.line(img, (320,240), (cx,cy), (0, 255, 0), 1)
          cv2.line(img, (320,240), (320,cy), (0, 255, 0), 1)
          cv2.line(img, (cx,cy), (320,cy), (0, 255, 0), 1)

        img=cv2.circle(img ,(cx,cy),2,(0,0,255),4) 
        temp=np.zeros(img.shape,np.uint8)
        contoursImg.append(temp)
        contoursImg[i]=cv2.drawContours(img,contours,i,(255,0,0), 3)


    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break



cap.release()
cv2.destroyAllWindows()


