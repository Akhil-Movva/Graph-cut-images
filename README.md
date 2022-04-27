# Graph-cut-images

## Assignment Description
In this assignment, composition of 2 images is performed using graphcuts. Further, we have also performed texture synthesis, which is the process of  producing a large image from a small sample image.

## Statement of help

### Required dependencies

#### Graph cut
1. cv2
2. numpy



### Texture synthesis
1. numpy
2. io,util from skimage
3. heapq
4. PIL from Image

#### Command to install cv2 in python
>pip install opencv-python

### Instructions to run the code
#### Graph cut
After changing the directory to ***Image-Composition*** directory, type the following command into the termainal and press 'ENTER' key.
>python GraphCut.py

#### Texture synthesis
After changing the directory to ***Texture-Synthesis*** directory, type the following command into the termainal and press 'ENTER' key.
>python TextureSynthesis.py

### Interpreting the output
#### Graph cut

 ##### Input Images
  
 ![sea_bird](https://user-images.githubusercontent.com/28916768/165418100-2cdb9867-2e16-4863-b116-ab93cf10eb87.jpg)
 ![tajmahal](https://user-images.githubusercontent.com/28916768/165418309-e5231f67-4a05-4861-aa47-119eac79d899.jpg)

  ##### Intermediate Outputs
  
  
  ##### Final Output
   Compositing new image into old one
   
  ![sea_bird_masked_tajmahal](https://user-images.githubusercontent.com/28916768/165418907-a1c8964d-d264-4755-867d-0576385b3ba6.jpg)

  #### Texture Synthesis
  
  ##### Input Image
  ![weave](https://user-images.githubusercontent.com/28916768/165419398-e7850793-4511-45f0-9135-0c78f130e20e.jpg)

  
  ##### Output Image
  
  Image generated with the help of min-cost path
  ![Texture_Synthesis_cut1](https://user-images.githubusercontent.com/28916768/165419557-b4a39576-6752-46a1-9954-20bd42181e5c.jpg)



 ## References
 
 1. https://pythonprogramming.net/grabcut-foreground-extraction-python-opencv-tutorial/
 2. https://www.youtube.com/watch?v=o1lEjkv5o_8&t=1s
 3. https://subscription.packtpub.com/book/web-development/9781788474443/4/ch04lvl1sec50/obtaining-an-object-mask-using-the-grabcut-algorithm
 4. https://devashi-choudhary.medium.com/texture-synthesis-generating-arbitrarily-large-textures-from-image-patches-32dd49e2d637
 







 
 
