import cv2
import numpy as np


def Morph():
    img1 = cv2.imread("car1.jpg",0)
    cv2.imshow("Frame",img1)
    cv2.waitKey(0)


    kernel = np.ones((5,5),np.uint8)
    image_ersion = cv2.erode(img1,kernel,iterations=1)
    image_dilation = cv2.dilate(img1,kernel,iterations=1)

    image_open = cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)
    image_close = cv2.morphologyEx(img1,cv2.MORPH_CLOSE,kernel)

    image_tophat = cv2.morphologyEx(img1,cv2.MORPH_TOPHAT,kernel)
    image_blackhat = cv2.morphologyEx(img1,cv2.MORPH_BLACKHAT,kernel)


    cv2.imshow("Erosion",image_ersion)
    cv2.waitKey(0)


    cv2.imshow("Dilate",image_dilation)
    cv2.waitKey(0)


    cv2.imshow("Open",image_open)
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




