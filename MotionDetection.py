import cv2
import math
import numpy as np
import matplotlib.pyplot as plt



def openImg(file):
    img = cv2.imread('images/' + file, cv2.IMREAD_COLOR)

    return img

def showImg(img):
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img, cmap='gray', interpolation='bicubic') # nearest, bilinear, bicubic
    plt.show()

def histClr(img):
    x_axis = np.zeros(255, np.int)

    plt.figure(figsize=[10, 8])

    for i, col in enumerate(['b', 'g', 'r']):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()
    return hist

def histGray(img):
    hist = cv2.calcHist(img, [0], None, [256], [0, 256])
    # plt.plot(hist, color='k')
    # plt.show()
    return hist

def compare(img1, img2):
    # img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    h, w = img1.shape[:2]
    grid = np.zeros((h, w, 3), np.int)
    grid[:,:, 0] = img1[:,:,0] - img2[:,:,0]

    histClr(grid)
    # showImg(grid)
    # showImg(img2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

f1 = '_MG_9711-2.jpg'
img1 = openImg(f1)

f2 = '_MG_9711-3.jpg'
img2 = openImg(f2)

compare(img1, img2)

