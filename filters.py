import cv2 
import numpy as np

def apply_colour_filter(image, filter_type):
    #make a copy of the image so the filter doesn't affect the original image
    #The colons specify the height and width of the image
    #[:,:,0]blue
    #[:,:,1]green
    #[:,:,2]red
    image_copy=image.copy()
    if filter_type=="red":
        image_copy[:,:,1]=0
        image_copy[:,:,0]=0
    elif filter_type=="green":
        image_copy[:,:,2]=0
        image_copy[:,:,0]=0
    elif filter_type=="blue":
        image_copy[:,:,2]=0
        image_copy[:,:,1]=0
    elif filter_type=="increase_red":
        image_copy[:,:,2]=cv2.add(image_copy[:,:,2], 50)
    elif filter_type=="decrease_blue":
        image_copy[:,:,0]=cv2.subtract(image_copy[:,:,0], 50)

    return image_copy

filter_img= "images.jpg"
image=cv2.imread(filter_img)
filter_type="original"
print("Press the following keys for filters:")
print("'r' for a red tint filter")
print("'b' for a blue tint filter")
print("'g' for a green tint filter")
print("'i' to increase the red tint filter")
print("'d' to decrease the blue tint filter")
print("'q' to quit the filter applier.")
while True:
    filtered_img=apply_colour_filter(image,filter_type)
    key=cv2.waitKey(0) & 0xFF

    if key==ord('r'):
        filter_type='red'
    elif key==ord('b'):
        filter_type="blue"
    elif key==ord('g'):
        filter_type='green'
    elif key==ord('i'):
        filter_type="increase_red"
    elif key==ord('d'):
        filter_type="decrease_blue"
    elif key==ord('q'):
        break
    else:
        print("Invalid input.")

cv2.destroyAllWindows()