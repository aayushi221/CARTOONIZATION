# CARTOONIZATION

 ![](https://socialify.git.ci/aayushi221/CARTOONIZATION/image?font=Inter&forks=1&issues=1&language=1&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Dark)

### Hi everyone!👋

This is a program to cartoonize an image without using complex procedures such as deep learning/ ML. We are going to use simple Open CV using python and numpy.

### About this program

In order to achieve such basic cartoon effect, we don't really need a powerful rendring software.
			We can easily use bilateral filter and some edge detection.

 ![](https://raw.githubusercontent.com/aayushi221/CARTOONIZATION/master/SHORT%20PROJECT%202/Cartoon.JPG)

#### How does it work?

1. Apply bilateral filter to reduce the color palette of the image.
2. Convert the original color image to grayscale
3. Apply median blur to reduce image noise in the resultant grayscale image.
4. Create an edge mask from the grayscale image using adaptive thresholding.
5. Combine the color image from step 1 with the edge mask from step

#### Pro tip

Use an image with higher contrast to get better results. :)

### Tech Stack 📂

 ![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
