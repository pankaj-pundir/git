import cv2
#import matplotlib.pyplot as plt
t=cv2.imread('book.jpg')
cv2.imshow("image",t)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)