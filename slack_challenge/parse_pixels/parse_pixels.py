#**********************************************************************************************************************#
#                                                                                                                      #
# This is an extremely simple way to parse through each pixel of an image and get it's RGBA value.                     #
# It's nothing special but would help alot for what we're trying to achieve.                                           #
# I've added comments for each line, though ask me if you dont understand anything.                                    #
# -Suchet                                                                                                              #
#                                                                                                                      #
#**********************************************************************************************************************#

# Python imaging library, version 1.1.6. Ask me for the library folder if you're having trouble installing it.
from PIL import Image
# Win32api. Using this for the Sleep() function to stop my code for any number of milliseconds i want.
import win32api

# Get a handle to an image. The argument has to be the exact filepath to your image.
# We replace ( \ ) with  ( \\ ) as the single ones are used to ( \n - new line ) and etc.
image = Image.open("C:\\Users\\sukhv\\Desktop\\Suchet\\interaccel_test2.7\\1A_stuff\\pics\\Capture.jpg")


# This is to get the handle to the pixels.
pixel = image.load()


# This holds the size of the image as a list. Eg: (x, y). Where x and y is the last pixel for each axis.
image_size = image.size
print(image_size)  # (336, 384)
image_x = image_size[0]
image_y = image_size[1]


# These are going to be incremented on each loop and then used for indexing.
increment_image_x = 0
increment_image_y = 0


# Now we are going to loop through each y pixel.
while (True):
    if ( increment_image_y == image_y ): # Last Y axis. Shift the X axis by 1 and start the Y axis all over again.
        increment_image_y = 0
        increment_image_x += 1
        if ( increment_image_x == image_x ):
            break
    else:
        print( pixel[increment_image_x, increment_image_y] )
        increment_image_y += 1

    win32api.Sleep(1) # Make it so our loop gets executed once in 1 ms so it doesnt slow our pc.
