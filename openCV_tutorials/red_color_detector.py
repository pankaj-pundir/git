#black=res
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
lines=[]
def center_of_contour(x_c):
    M=cv2.moments(x_c)
    #print(M['m00'])
    return (int(M['m10']/(M['m00'])),int(M['m01']/(M['m00'])))
def x_cord_contour(x_c):
    if cv2.contourArea(x_c) >9:
        return center_of_contour(x_c)[0]
    
def image_color_track(black):
    gray=cv2.cvtColor(black,cv2.COLOR_RGB2GRAY)
    can=cv2.Canny(gray,3,20)
    con_img,contours,hierarchy=cv2.findContours(can,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   
    try:
        sorted_cont=sorted(contours,key=cv2.contourArea,reverse=True)
        cv2.drawContours(black,sorted_cont[0],-1,(0,255,0),5)
        try:
            lines.append((center_of_contour(sorted_cont[0])+lines[-1])/2)
        except:
            lines.append((center_of_contour(sorted_cont[0])))
    finally:
        if len(lines)>50:
            lines.pop(0)
        if len(lines)>0:
            for i in range(len(lines)-1):
                cv2.line(black,lines[i],lines[i+1],(255,255,255),3)
        return black
def color_extractor(image): 
    #hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv=image
    lower_lim=np.array([0,0,0],dtype='uint8')
    upper_lim=np.array([10,10,255],dtype='uint8')
    mask=cv2.inRange(hsv,lower_lim,upper_lim)
    res=cv2.bitwise_and(hsv,hsv,mask=mask)
    kernel=np.ones((10,10),np.uint8)
    res=cv2.dilate(res,kernel,iterations=2)
    res=cv2.blur(res,(10,10))
    #return res
    return image_color_track(res)

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    #frame=cv2.convertScaleAbs(frame)
    cv2.imshow("skecth",color_extractor(frame))
    if cv2.waitKey(1) & 0xFF ==ord('q') :
        break
cap.release()
cv2.destroyAllWindows()