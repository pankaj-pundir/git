# import cv2
# import matplotlib.pyplot as plt
# def sketch(image):
#     img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     img_bl=cv2.GaussianBlur(img_gray,(5,5),0)
#     canny=cv2.Canny(img_bl,10,80)
#     ret,mask=cv2.threshold(canny,70,255,cv2.THRESH_BINARY_INV)
#     return mask
# cap=cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("skecth",sketch(frame))
#     if cv2.waitKey(1) & 0xFF ==ord('q') :
#         break
# #cap.release()
# cv2.destroyAllWindows()
# cv2.waitKey(1)




import cv2
import numpy as np

def al_show(image):
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

lines=[]
def center_of_contour(x_c):
    M=cv2.moments(x_c)
    return (int(M['m10']/M['m00']+1),int(M['m01']/M['m00']+1))
def x_cord_contour(x_c):
    if cv2.contourArea(x_c) >9:
        return center_of_contour(x_c)[0]
    
def image_color_track(black):
    gray=cv2.cvtColor(black,cv2.COLOR_RGB2GRAY)
    can=cv2.Canny(gray,3,20)
    con_img,contours,hierarchy=cv2.findContours(can,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(black,contours,-1,(0,255,0),5)
    lines.append(center_of_contour(contours[0]))
    if len(lines)>0:
        for i in range(len(lines)-1):
            cv2.line(black,lines[i],lines[i+1],(255,255,255),3)
    return black


def color_extractor(image): 
    hsv=image
    lower_lim=np.array([50,0,0])
    upper_lim=np.array([255,100,100])
    mask=cv2.inRange(hsv,lower_lim,upper_lim)
    res=cv2.bitwise_and(hsv,hsv,mask=mask)
    return image_color_track(res)


al_show(color_extractor('hibiscus.jpg'))
frame.dtype


# cap=cv2.VideoCapture(0)
# ret,frame=cap.read()
# #frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
# plt.imshow(frame)
# #print(frame)
# frame.dtype
# # while True:
# #     ret,frame=cap.read()
# #     frame=cv2.convertScaleAbs(frame)
# #     cv2.imshow("skecth",color_extractor(frame))
# #     if cv2.waitKey(1) & 0xFF ==ord('q') :
# #         break
# cap.release()
# cv2.destroyAllWindows()