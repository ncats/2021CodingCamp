
import cv2  
#loads an image from the specified file
import numpy
#When you import a module via import numpy. the numpy package is bound to the local variable numpy . The import as syntax simply allows you to bind the import to the local variable name of your choice (usually to avoid name collisions, shorten verbose module names, or standardize access to modules with compatible APIs).
img = cv2.imread('C:/Users/shapirolm/Desktop/Python/test/ColorfulImage.png') 
 #loads an image from the specified file.
blue, green, red = cv2.split(img)
 #The cv2. split() function splits the source multichannel image into several single-channel images. The cv2. merge() function merges several single-channel images into a multichannel image.
 
zeros = numpy.zeros(blue.shape, numpy.uint8)
#Python function is used to create a matrix full of zeroes. numpy.zeros () in Python can be used when you initialize the weights during the first iteration in TensorFlow and other statistic tasks. 
 
blueBGR = cv2.merge((blue,zeros,zeros))
greenBGR = cv2.merge((zeros,green,zeros))
redBGR = cv2.merge((zeros,zeros,red))
#The cv2. merge() function merges several single-channel images into a multichannel image.


cv2.imshow('blue BGR', blueBGR)
cv2.imshow('green BGR', greenBGR)
cv2.imshow('red BGR', redBGR)
 #The cv2.imshow () method in Python is used to display an image in a window. The window automatically fits the image size.
cv2.waitKey(0)
#cv2 waitkey () allows you to wait for a specific time in milliseconds until you press any button on the keyword
cv2.destroyAllWindows()
#If you have multiple windows open and you do not need those to be open, you can use that code to close them all

# this is me writing a random sentence



