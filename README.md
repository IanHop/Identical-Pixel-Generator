# Identical-Pixel-Generator
* Python script that tells you how many attempts it would take to randomly generate an image with X pixels. Spoiler it take a long time.
* Each generated pixel is composed of 3 values 0-255 which make up one RGB pixel. Currently the script will just generate a random pixel map and then see how long it takes to randomly generate a second map that is exactly the same.
* 256x256x256=16777216, so there is a 1/16777216 chance to just generate a 1px image. Now imaging the odds of generating a normal sized image.
* I have never succesfully genrated the same 2 pixel image. Maybe you are lucky.

# Running the Script
* Type `python color_guess.py [x]` x is the number of pixels in the image.
* Let her rip.


# This is great for warming up your computer or even your house on a cold winters day. Use at your own risk.
