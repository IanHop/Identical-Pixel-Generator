#Created by IanHop for some reason 01/22/20
import sys; sys.dont_write_bytecode = True
import random
import time
from datetime import datetime, date

#Tested putting all of the numbers in a single array, but it was actually twice as slow as having arrays in arrays

def run(numPixels):
    if type(numPixels) != int or numPixels < 1:
        print("Please enter the number of pixels greater than 0 as an int")
        sys.exit(0);

    pixelColorMap = [];

    print("Generating pixel color map")
    i = 0
    while i < numPixels:
        pixelColorMap.append(generate_pixel_color());
        i += 1

    startTime = datetime.now()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Start time: " + startTime.strftime("%H:%M:%S"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Random {0} pixel map generated".format(numPixels))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(pixelColorMap);
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Test begins in:")
    i = 0
    while(i < 5):
        print(i + 1)
        i += 1
        time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~Start~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    attempts = 0;
    foundPixelColorMap = [];

    while (True):
        tempPixelcolorMap = []
        attempts += 1;

        for pixelColor in pixelColorMap:
            tempPixelcolorMap.append(generate_pixel_color())


        print("Attempt - {0}".format(attempts))
        if (tempPixelcolorMap == pixelColorMap):
            foundPixelColorMap = tempPixelcolorMap
            break

    pixelString = "PIXEL"
    if numPixels > 1:
        pixelString += "S"


    print(pixelString + "ACTUALLY FOUND - {0} attempts!!!".format(attempts));
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(foundPixelColorMap);
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Elapsed time: " + str(datetime.now() - startTime))


def generate_pixel_color():
    tempPixelColor = []
    tempR = random.randint(0, 255);
    tempG = random.randint(0, 255);
    tempB = random.randint(0, 255);
    tempPixelColor.append(tempR);
    tempPixelColor.append(tempG);
    tempPixelColor.append(tempB);

    return tempPixelColor

if __name__ == "__main__":
    run(int(sys.argv[1]))
