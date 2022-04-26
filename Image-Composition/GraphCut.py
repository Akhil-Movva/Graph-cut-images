#This file contains implementation of graphcut images

import cv2
import numpy as np

image = cv2.imread('sea_bird.jpg')

#specifying the background and foreground model
fgModel = np.zeros((1,65),np.float64)
bgModel = np.zeros((1,65),np.float64)



#  MOUSECALL BACK FUNCTIONS BEGIN
show_img = np.copy(image)

# Define some constants
mouse_pressed = False
x = y = w = h = 0

# Define the mouse callback function to draw a rectangle on the image
def mouse_callback(event, _x, _y, flags, param):
    global show_img, x, y, w, h, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x, y = _x, _y
        show_img = np.copy(image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_img = np.copy(image)
            cv2.rectangle(show_img, (x, y),
                          (_x, _y), (0, 255, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        w, h = _x - x, _y - y
# MOUSECALL BACK FUNCTION END

# SELECT AREA WITH RECTANGLE WITH MASK AND PRESS A KEY BEGIN

# Display the image
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# after the rectangle has been completed
# and the A button on the keyboard has been pressed,
# We'll close the window
while True:
    cv2.imshow('image', show_img)
    k = cv2.waitKey(1)

    if k == ord('a') and not mouse_pressed:
        if w*h > 0:
            break

cv2.destroyAllWindows()

#SELECT AREA WITH RECTANGLE WITH MASK AND PRESS A KEY END

#GRAB MASK AND CREATE DYNAMIC MASK BEGIN

# Call cv2.grabCut to create an object mask based on the rectangle
sMask = np.zeros(image.shape[:2],np.uint8)

(sMask, bgModel, fgModel)= cv2.grabCut( image, sMask, (x, y, w, h), bgModel,fgModel, 5, cv2.GC_INIT_WITH_RECT )

# the output mask has four possible output values, marking each pixel
# in the mask as (1) definite background, (2) definite foreground,
# (3) probable background, and (4) probable foreground
values = (
	("Definite Background", cv2.GC_BGD),
	("Probable Background", cv2.GC_PR_BGD),
	("Definite Foreground", cv2.GC_FGD),
	("Probable Foreground", cv2.GC_PR_FGD),
)

# loop over the possible mask values
for (name, value) in values:
	# construct a mask that for the current value
	print("[INFO] showing mask for '{}'".format(name))
	valueMask = (sMask == value).astype("uint8") * 255

	# display the mask so we can visualize it
	cv2.imshow(name, valueMask)
	cv2.waitKey(0)

new_mask = (sMask == cv2.GC_PR_FGD).astype("uint8") * 255
cv2.imshow( "new_mask", new_mask )
cv2.waitKey(0)

# we'll set all definite background and probable background pixels
# to 0 while definite foreground and probable foreground pixels are
# set to 1
valueMask = (sMask == cv2.GC_PR_FGD).astype("uint8") * 255

outputMask = np.where(( sMask == cv2.GC_BGD) | ( sMask == cv2.GC_PR_BGD),0, 1)

# scale the mask from the range [0, 1] to [0, 255]
outputMask = (valueMask * 255).astype("uint8")

# we'll set all definite background and probable background pixels
# to 0 while definite foreground and probable foreground pixels are
# set to 1

# apply a bitwise AND to the image using our mask generated by
# GrabCut to generate our final output image
output = cv2.bitwise_and( new_mask, new_mask, mask=outputMask)
cv2.imshow("GrabCut Output", output)
cv2.waitKey(0)

cv2.imwrite('sea_bird_mask.png', output )



#GRAB MASK AND CREATE DYNAMIC MASK END
# READ DESTINATION IMAGE AND NEWLY CREATED MASK BEGIN


dst = cv2.imread("tajmahal.jpg")
# read dimensions to set tailor or Tdynamic positions
height_dst, width_dst, channels_dst = dst.shape
print( '1', height_dst, width_dst, channels_dst )
src_mask = cv2.imread("sea_bird_mask.png")
height_mask, width_mask, channels_mask = src_mask.shape
print( '2',  height_mask, width_mask, channels_mask )
#READ DESTINATION IMAGE AND NEWLY CREATED MAS END

#SET CENTER POSITION SEAMLESS CLONE BEGIN

# dynamically set center position
monoMaskImage = cv2.split( image )[0] # reducing the mask to a monochrome
br = cv2.boundingRect(monoMaskImage) # bounding rect (x,y,width,height)
centerOfBR = (br[0] + br[2] // 2, br[1] + br[3] // 2)

output = cv2.seamlessClone( image, dst, src_mask, centerOfBR, cv2.NORMAL_CLONE )

# save result

cv2.imwrite("sea_bird_tajmahal.jpg", output)

#SET CENTER POSITION SEAMLESS CLONE END