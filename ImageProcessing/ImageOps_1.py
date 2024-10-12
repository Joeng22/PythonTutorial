'''
Notes
Reference : https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. 
It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. 
Two basic morphological operators are Erosion and Dilation.

Then its variant forms like Opening, Closing, Gradient etc.

'''

import cv2
import numpy as np


def Morph():
    img1 = cv2.imread("car1.jpg",0)
    cv2.imshow("Frame",img1)
    cv2.waitKey(0)


    kernel = np.ones((5,5),np.uint8)
    # A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
    image_ersion = cv2.erode(img1,kernel,iterations=1)  

    #It is just opposite of erosion. Here, a pixel element is '1' if at least one pixel under the kernel is '1'. 
    #Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. 
    # So we dilate it. Since noise is gone, they won't come back, but our object area increases.
    image_dilation = cv2.dilate(img1,kernel,iterations=1)

    #Opening is just another name of erosion followed by dilation. It is useful in removing noise, as we explained above
    image_open = cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)

    #Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.
    image_close = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)

    #It is the difference between dilation and erosion of an image.
    image_gradient = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)


    #It is the difference between input image and Opening of the image.
    image_tophat = cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,kernel)
    
    #It is the difference between the closing of the input image and input image.
    image_blackhat = cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,kernel)


    cv2.imshow("Erosion",image_ersion)
    cv2.waitKey(0)


    cv2.imshow("Dilate",image_dilation)
    cv2.waitKey(0)


    cv2.imshow("Open",image_open)
    cv2.waitKey(0)

    cv2.imshow("Gradient",image_gradient)
    cv2.waitKey(0)

    cv2.imshow("Close",image_close)
    cv2.waitKey(0)


    cv2.imshow("TopHAT",image_tophat)
    cv2.waitKey(0)


    cv2.imshow("BlackHat",image_blackhat)
    cv2.waitKey(0)    

if __name__=="__main__":

    Morph()

    '''
    ImagePath = "car1.jpg"
    img1 = cv2.imread(ImagePath,-1)
    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame",img1)
    cv2.imshow("Frame2",img1_gray)

    edges = cv2.Canny(img1_gray,100,200)
    cv2.imshow("Edges",edges)
    cv2.waitKey(0)
    '''




