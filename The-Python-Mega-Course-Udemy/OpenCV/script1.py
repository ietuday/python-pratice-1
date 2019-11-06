import cv2

img = cv2.imread("galaxy.jpg", 0) # 1 for color, 0 for greyscale(it has only one band), -1 for alpha(transparency capabilities)

print(type(img))

print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(0)
"""
0 - If the user presses any button then the image window closes
2000 - 2000 milliseconds later the image is closed
"""
cv2.destroyAllWindows()
