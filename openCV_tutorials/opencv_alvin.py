import cv2
import numpy as np
import matplotlib.pyplot as plt

def cuber_effect(image,frame_size=(480,848),kernel_size=(10,14)):
    '''frame_size input size of frame in tuple , kernel size in tuple x and y axis'''
    no_of_cubes=(int(frame_size[0]/kernel_size[0]),int(frame_size[1]/kernel_size[1]))
    for i in range(no_of_cubes[0]):
        for j in range(no_of_cubes[1]):
            image[i*kernel_size[0]:(i+1)*kernel_size[0],j*kernel_size[1]:(j+1)*kernel_size[1]]=\
            cv2.flip(image[i*kernel_size[0]:(i+1)*kernel_size[0],j*kernel_size[1]:(j+1)*kernel_size[1]],1)
    return image

def pim(image):
	plt.imshow(image)

def im(image,name="image"):
	''' image is the image file willing to display , 
	name the name of window '''
	cv2.imshow(name,image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	for i in range(5):
	    cv2.waitKey(1)

def black_image(width,height):
	''' Return a black_image with defined size'''
	return np.zeros((512,512,3),np.uint8)

def webCamImage():
	cap = cv2.VideoCapture(0)
	if (cap.isOpened()== False): 
		print("Error opening image stream or file")
	ret, frame = cap.read()
	return frame

def videoProcessing(input_channel=0):
	''' Do define videoFunc to process the frame in it , input the input parameter'''
	cap = cv2.VideoCapture(input_channel)
	if (cap.isOpened()== False): 
	  print("Error opening video stream or file")

	while(cap.isOpened()):
	  # Capture frame-by-frame
	    ret, frame = cap.read()
	    if ret == True:
	        cv2.imshow('Frame',frame)
	        out.write(temp)
	        if cv2.waitKey(25) & 0xFF == ord('q'):
	            cv2.destroyAllWindows()
	            for i in range(5):
	                cv2.waitKey(1)
	            break;
	  # Break the loop
	    else: 
	        break
	cap.release()
	return True
