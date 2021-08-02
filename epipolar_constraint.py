import cv2 as cv
import numpy as np
def epipolar_idx_vals(matchess, list_kp1s, list_kp2s, delta):
    # get the fundamental matrices
    Fs = []
    for i in range(len(delta)):
        x, y = cv.findFundamentalMat(list_kp1s[i], list_kp2s[i], cv.FM_RANSAC)
        Fs.append(x)
    # compute the epipolar constraint for each set of matching points
    valss = []
    for i in range(len(delta)):
        vals = []
        for j in range(len(list_kp1s[i])):
            left = np.array([list_kp1s[i][j][0], list_kp1s[i][j][1], 1])
            right = np.array([list_kp2s[i][j][0], list_kp2s[i][j][1], 1])
            vals.append(np.absolute(np.dot(np.dot(left, Fs[i]), np.transpose(right))))
        valss.append(vals)
        bigs = []
    for i in range(len(delta)):
        big = list(np.argsort(valss[i]))
        big.reverse()
        bigs.append(big)
        # print(bigs)
    return bigs
