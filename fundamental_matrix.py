# We are going to detect moving objects, just by comparing 2 images taken at
# slightly different viewpoints at diffferent times. This would be an easier
# task if the images were not at different viewpoints since we could then apply
# the simple technique of background subtraction to figure out which objects
# have moved. In this task, we are trying to detect moving objects but when
# the camera angle is changing.


# first we have our import statements
import numpy as np
import pandas as pd
import cv2 as cv
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
from matching import get_keypoints
from epipolar_constraint import epipolar_idx_vals
import os

# We will compare the 1st frame to the 2nd, the 3rd, the 6th, the 11th, the 21st, and the 41st frame
# In these frames an airborne object is moving. The hope is to be able to detect this movement
# Intuitively, as the frame difference is larger (the object has moved further from it's original position) and it
# should be easier to track

# step 1: retrieve the images
file_names = sorted(os.listdir('images'))
start_idx = 1
print(file_names)
im1 = cv.imread('images/' + file_names[0], cv.IMREAD_GRAYSCALE)
# print(im1.shape)
im2s = []
delta = [1, 2, 5, 10, 20, 40]
for i in range(len(delta)):
  print(delta)
  im2s.append(cv.imread('images/' + file_names[start_idx + i], cv.IMREAD_GRAYSCALE))

# step 2 & 3: get a set of matching points to compute fundemental matrix
# get list of matching keypoints
matchess, frame1_keypoints, frame2_keypoints, kp1, kp2s = get_keypoints(im1, im2s, delta) # matches, frame 1 keypoints, frame 2 keypoints

# If there are enough matching keypoints, we can compute a fundamental matrix, which
# relates any point in one frame to another frame by a simple 3 x 3 matrix.
# An example, would be like a tree in the first frame in matched to the same tree in the second frame even if the image
# is taken at a different angle.
# The relation is known as the epipolar constraint where
# (x1, y1, 1) * F * (x2, y2, 1)^T = 0
# Thus, if 2 points that have not moved in the image are related, then their epipolar
# constrint should be close to 0 and if something has moved then the epipolar constraint
# should be further away from 0

# step 4: compute the fundamental matrix & epipolar constraint for each set of matched points
# get the sorted set of matching keypoints by index
bigs = epipolar_idx_vals(matchess, frame1_keypoints, frame2_keypoints, delta)

# step 5: output results
for i in range(len(delta)):
    final_matches = []
    for j in range(200):
        if(frame2_keypoints[i][bigs[i][j]][1] < 1200):
            print(j)
            final_matches.append(matchess[i][bigs[i][j]])
            break
    img3 = cv.drawMatches(im1,kp1,im2s[i],kp2s[i],final_matches,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imwrite('results/' + str(i) + '.png', img3)
    cv.imshow('frame', img3)
    if cv.waitKey(1000) & 0xFF == ord('q'):
        break
