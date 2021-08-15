## Moving Object Detection with the Fundamental Matrix
---------
A very important principle in Computer Vision is that if we have two images of the same general area but at different angles we can compute a fundamental matrix.
This fundamental matrix is able to relate points between the two images with the epipolar constraint.

If ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20(x_1,%20y_1)) and ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20(x_2,%20y_2)) correspond to the same point just in different images and ![formula](https://render.githubusercontent.com/render/math?math=\color{white}F) is the fundamental matrix, then the relation, known as the epipolar constraint, is that ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20[x_1,%20y_1,%201]%20F%20[x_2,%20y_2,%201]^T%20=%200)

Now, we won’t have this always equal exactly 0. If an object has moved in the two images we have then the epipolar relation of the object points will be further away from 0. It will be high. Essentially, we have dynamic points (moving points) have a high epipolar relation and static points to have a low epipolar relation.

By Finding matching points with a matching algorithm and computing the epipolar constraint of these points, we can figure out which objects are likely to be moving.

## Results
We evaluated the performance of the fundamental matrix with a shaky video sequence of a moving helicopter. The video consists of image frames and each frame is essentially the same image at slightly different angles with exception to the helicopter which would be at different locations.

We looked at images that were 1, 2, 5, 10, 20, and 40 frames apart. The larger the difference the further away the helicopter has moved from it's original location. The hope is that the pixel points corresponding to the helicopter will break the epipolar constraint the most (be far away from 0).

### 1 Frame Apart
The helicopter point corresponded to the points that gave the 6th largest epipolar constraint value.
![Screenshot](results/0.png)

### 2 Frames Apart
The helicopter point corresponded to the points that gave the 149th largest epipolar constraint value.
![Screenshot](results/1.png)

### 5 Frames Apart
The helicopter point corresponded to the points that gave the 119th largest epipolar constraint value.
![Screenshot](results/2.png)

### 10 Frames Apart
The helicopter point corresponded to the points that gave the 131st largest epipolar constraint value.
![Screenshot](results/3.png)

### 20 Frames Apart
The helicopter point corresponded to the points that gave the 43rd largest epipolar constraint value.
![Screenshot](results/4.png)

### 40 Frames Apart
The helicopter point corresponded to the points that gave the 32nd largest epipolar constraint value.
![Screenshot](results/5.png)

### Analysis
We see a trend with exception to when it is 1 frame apart that as the helicopter is further away from it's original point it will be one of the points with higher epipolar constraint values. Also, if we just looked above the horizon the helicopter is conistently the first point with the highest epipolar constraint value. This method can be used to find moving points of interest. 
