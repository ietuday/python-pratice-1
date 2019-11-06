import cv2
img = cv2.imread("galaxy.jpg",0)

#getting the shape(rows and columns)
print(img.shape)
#Getting the dimensions. 2 = B&W image, 3 = RGB
print(img.ndim)

#resize image. parameter 1 = the image we want to resize. parameter 2 = new size (tuple)
#resized_img = cv2.resize(img,(1000,500))

#Keep the img ratio while resizing
resized_img = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imwrite("Galaxy_resized.jpg",resized_img)

#Showing the img. parameter 1 = name of the window. parameter 2 = what we want to show
cv2.imshow("Galaxy",resized_img)

#When to close the window. 0 = any button, 2000 example = miliseconds
cv2.waitKey(0)
#cv2.waitKey(2000) 2 seconds
cv2.destroyAllWindows()
