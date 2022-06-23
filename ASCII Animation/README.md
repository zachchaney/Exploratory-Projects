# ASCII Animation

This Python program converts a GIF or image file into an ASCII representation.

<p align="center">
  <img src="https://github.com/zachchaney/Exploratory-Projects/blob/main/ASCII%20Animation/nyan_cat_ascii.gif" width="45%" />
  <img src="https://github.com/zachchaney/Exploratory-Projects/blob/main/ASCII%20Animation/nyan_cat.gif" width="45%" />
</p>

## Usage

From the command line, enter:

    py gif_to_ascii.py <File_to_Convert>

A file named <File_to_Convert>_ascii will be saved to the location of the original file.

## Algorithm

Below is pseudocode of the gif_to_ascii.py file.

> Convert the GIF to an array of image files  
> **for each** image in the array **do**:  
> &nbsp;&nbsp;&nbsp;&nbsp; Convert the image to grayscale  
> &nbsp;&nbsp;&nbsp;&nbsp; Scale down the image  
> &nbsp;&nbsp;&nbsp;&nbsp; Convert each pixel to 1 of 11 characters depending on the brightness of the pixel  
> &nbsp;&nbsp;&nbsp;&nbsp; Reassemble the pixels into an image  
> Reassemble the array of converted images back into a GIF

We scale down the image such that when the pixels are converted to characters the resulting image is congruent to the original image.
