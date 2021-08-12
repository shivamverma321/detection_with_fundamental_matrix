## Moving Object Detection with the Fundamental Matrix 
---------
A very important principle in Computer Vision is that if we have two images of the same general area but at different angles we can compute a fundamental matrix.
This fundamental matrix is able to relate points between the two images with the epipolar constraint. 

If ![formula](https://render.githubusercontent.com/render/math?math=(x_1, y_1)) correspond to the same point just in different images, then the relation is that  <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix} x_1 & y_1 & 1 \end{bmatrix} F \begin{bmatrix} x_2 \\ y_2 \\ 1 \end{bmatrix} = 0" />. 

Now, we won’t have this always equal exactly 0. If an object has moved in the two images we have then the epipolar relation of the object points will be further away from 0. It will be high. Essentially, we have dynamic points (moving points) have a high epipolar relation and static points to have a low epipolar relation. 

By Finding matching points with a matching algorithm and computing the epipolar constraint of these points, we can figure out which objects are likely to be moving. 

## Results 

images 
