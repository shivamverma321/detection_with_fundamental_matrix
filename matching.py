import cv2 as cv
import numpy as np
from PIL import Image


def get_keypoints(im1, im2s, delta):
    # step 1 find keypoints of the image
    # there are multiple ways to do this: SIFT & ORB for now we are going to try out ORB
    orb = cv.ORB_create()
    kp2s = []
    des2s = []
    kp1, des1 = orb.detectAndCompute(im1,None)
    for i in range(len(delta)):
      x, y = orb.detectAndCompute(im2s[i],None)
      kp2s.append(x)
      des2s.append(y)

    # now run a matching algorithm to match keypoints
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matchess = []
    for i in range(len(delta)):
      matches = bf.match(des1, des2s[i])
      matches = sorted(matches, key = lambda x:x.distance)
      matchess.append(matches)

    list_kp1s = []
    list_kp2s = []
    for i in range(len(delta)):
        list_kp1s.append(np.array([kp1[mat.queryIdx].pt for mat in matchess[i]]))
        list_kp2s.append(np.array([kp2s[i][mat.trainIdx].pt for mat in matchess[i]]))

    return matchess, list_kp1s, list_kp2s, kp1, kp2s
