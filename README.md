# Pixel-Generator-Counter
* Stupid python script that tells you how many attempts it would take to generate an image with X pixels. Spoiler it take a long time.
* Each generated pixel is composed of 3 values 0-255 which make up on RGB pixel. Currently the script will just generate a random pixel map and then see how long it takes to generate a second map that is exactly the same.
* 256*256*256=16777216, so there is a 1/16777216 chance to generate the same 1 pixel image.
* I have never succesfully genrated the same 2 pixel image. Maybe you are lucky.

# Running the Script
* type `python color_guess.py [x]` x is the number of pixels in the image.
* watch her rip
