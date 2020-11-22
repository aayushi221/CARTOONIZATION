# CARTOONIZATION
Hi everyone!

This is a program to cartoonize an image without using complex procedures such as deep learning/ ML. We are going to use simple Open CV using python and numpy.

In order to achive such basic cartoon effect, we don't really need a powerful rendring software.
We can easily use bilateral filter and some edge detection.


1.Bilateral filter- Reduces the colour palette


2.Edge detection- Allows production of bold silhouettes

This what is happening in this small project:


STEP 1: Apply bilateral filter to reduce the color palette of the image.

STEP 2: Convert the original color image to grayscale

STEP 3: Apply median blur to reduce image noise in the resultant grayscale           image.

STEP 4: Create an edge mask from the ggrayscale image using adaptive                 thresholding.

STEP 5: Combine the color image from setpe 1 with the edge mask from step 4.


Easy peasy!


Pro tip(jk): Use an image with higher contrast to get better results. :)






Last but not the least,


I would like to thank MACHINE LEARNING INDIA for such amazing small tutorials.
