from PIL import Image
import numpy as numpy

print ("Enter image name and extension as one")

image_name= input()
image_convert = Image.open(image_name)
image_convert = (np.array(image_convert))

red = image_convert[:,:,0].flatten()
green = image_convert[:,:,1].flatten()
blue = image_convert[:,:,2].flatten()
label = [1]

output = np.array(list(label) + list(red) + list(green) + list(blue),np.uint8)
output.tofile("output")
