# Graph-cut-images

## Assignment Description
In this assignment, composition of 2 images is performed using graphcuts. Further, we have also performed texture synthesis, which is the process of  producing a large image from a small sample image.

## Statement of help

### Required dependencies

#### Graph cut
1. cv2
2. numpy



#### Texture synthesis
1. numpy
2. io,util from skimage
3. heapq
4. PIL from Image

#### Command to install cv2 in python
>pip install opencv-python

### Instructions to run the code
#### Graph cut
1. After changing the directory to ***Image-Composition*** directory, type the following command into the termainal and press 'ENTER' key.
>python GraphCut.py
2. After running the above command, the input image(sea_bird) opens in a new window. Then rectangular patch containing the bird is selected and lower case letter 'a' should be pressed to confirm the selection of the object.
3. After confirming the selection, you will get a new named window named definite background and then after pressing any letter on the keyboard you will get a window named probable background and again pressing any letter on the keyboard you will get definite foreground.
4. We will continue the process described above until we see a window named Outline_Foreground_Information.
5. At this point, we have our composited image in the ***Image-Composition*** directory.

#### Texture synthesis
After changing the directory to ***Texture-Synthesis*** directory, type the following command into the termainal and press 'ENTER' key.
>python TextureSynthesis.py

**Note**: Texture synthesis is taking about 15-20 minutes to generate the output.

### Interpreting the output
#### Graph cut

 ##### Input Images
  
 ![sea_bird](https://user-images.githubusercontent.com/28916768/165418100-2cdb9867-2e16-4863-b116-ab93cf10eb87.jpg)
 ![tajmahal](https://user-images.githubusercontent.com/28916768/165418309-e5231f67-4a05-4861-aa47-119eac79d899.jpg)

  ##### Intermediate Outputs
   Generated Mask
   
  ![sea_bird_mask](https://github.com/Akhil-Movva/Graph-cut-images/blob/main/Image-Composition/sea_bird_mask.png)
  
  Image showing overlap based on the mask
  
  ![Destination_Trasparant](https://github.com/Akhil-Movva/Graph-cut-images/blob/main/Image-Composition/Destination_Trasparant.jpg)
  
  Image showing cut on the source image
  Here, the part inside the green boundary will be combined with the target image to achieve image composition
  ![outline_foreground_info](https://github.com/Akhil-Movva/Graph-cut-images/blob/main/Image-Composition/Outline_ForeGround_Info.jpg)

  Link to the text file containing pixels of the cut
  
  https://github.com/Akhil-Movva/Graph-cut-images/blob/main/Image-Composition/pixels.txt
  
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
 







 
 
