#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:57:23 2018

@author: root
"""

from opencv_alvin import *
#im(rose)
import pytesseract as pyt
def remove_text(img):
    h=img.shape[0]
    boxes=pyt.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        charLen_x=int((int(b[3])-int(b[1]))*0.5)
        charLen_y=int((int(b[4])-int(b[2]))*0.5)
        if charLen_x>img.shape[0]*0.3 or charLen_y>img.shape[1]*0.3:
            continue
        else:
            img = cv2.rectangle(img, (int(b[1])-charLen_x,h - int(b[2])+charLen_y), (int(b[3])+charLen_x, h - int(b[4])-charLen_y), (255, 255, 255), -1)
    im(img,"after removing the text")
    return img

def bar_graph_detector(img_org):
    ''' img should be grayscale and enhanced without text'''
    kernel=np.ones((5,5),np.uint8)
    img=cv2.morphologyEx(img_org,cv2.MORPH_CLOSE,kernel,iterations=1)
    #img=cv2.dilate()
    #pim(img)
    img=remove_text(img)
    #img=cv2.blur(img,(3,3))
    canny_edges=cv2.Canny(img,20,100)
    im(canny_edges,'canny images')
    ci,contour,hierarchy=cv2.findContours(canny_edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    count=0
    disp=img_org
    tot_len=len(contour)
    if tot_len<2:
        return (0,0,0)
    for c in contour:

        #accuracy=0.003*cv2.arcLength(c,True)
        #approx=cv2.approxPolyDP(c,accuracy,True)
        hull=cv2.convexHull(c)
        approx=hull
        if 4<=len(approx)<=7:
            count+=1
            disp=cv2.drawContours(disp,[c],0,(255,0,0),1)
        else:
            disp=cv2.drawContours(disp,[c],0,(0,0,255),1)
            #print(len(approx))
    #print(str("accuracy is : ")+str(count/tot_len)+str(" ")+str(tot_len))
    return (disp,count,tot_len)
bar=cv2.imread('bar_graph_png/1.jpg')
im(bar)
