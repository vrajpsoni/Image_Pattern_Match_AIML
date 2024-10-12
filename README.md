# Matching image patterns with OpenCV-Python

A Python program to match a pattern from a given image against a database of existing images. We'll use OpenCV for image processing and assume that the existing images are stored in a specific directory.

## Getting started

Prerequisites for running the code are:

Python = 3.9<br/>
python-opencv = 4.10.0.84<br/>

or

```
pip install opencv-python
```

## Features

Here's a high-level outline of the steps:
- Load the pattern image.
- Iterate through the images in the database directory
- Use cv2.matchTemplate to find the pattern in each database image.
- Keep track of the best match.

## Usage

Inside the project's directory run:

```
python image_pattern_match.py
```
You can find sample images in the Image_Pattern_Gallery folder and the image to be matched is source_pattern_1.jpg

### Results

This script will scan through all images in the Image_Pattern_Gallery and find the one that best matches the given pattern image. The result will display the name of the image with the highest similarity score. 

------

## Keywords

#Vraj #VrajSoni #vrajsoni.com #UMass #GoBeacons #UMassBoston #Beacon #UMassBeacons #AIInstitute
#Python #openCV #imageProcessing #AI #ML 