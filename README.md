## Moving Object Detection with the Fundamental Matrix 
---------
A very important principle in Computer Vision is that if we have two images of the same general area but at different angles we can compute a fundamental matrix.
This fundamental matrix is able to relate points between the two images with the epipolar constraint. 

If ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20(x_1,%20y_1)) and ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20(x_2,%20y_2)) correspond to the same point just in different images and ![formula](https://render.githubusercontent.com/render/math?math=\color{white}F) is the fundamental matrix, then the relation is that ![formula](https://render.githubusercontent.com/render/math?math=\color{white}%20[x_1,%20y_1,%201]%20F%20[x_2,%20y_2,%201]^T%20=%200)

Now, we won’t have this always equal exactly 0. If an object has moved in the two images we have then the epipolar relation of the object points will be further away from 0. It will be high. Essentially, we have dynamic points (moving points) have a high epipolar relation and static points to have a low epipolar relation. 

By Finding matching points with a matching algorithm and computing the epipolar constraint of these points, we can figure out which objects are likely to be moving. 

## Results 

https://render.githubusercontent.com/render/math?math=\color{white}F
