import cv2
import os

list1 = os.listdir()
list1.remove("script1.py")
list1.remove("sample-images.zip")

for i in list1:
    img  = cv2.imread(i,1)
    img2 = cv2.resize(img,(100,100))
    cv2.imwrite(i,img2)

'''
Another more efficient way will be to use glob library. This library looks for a match
pattern
import glob2
list1 = glob2.glob("*.jpg")

That instruction takes all the file names that ends with ".jpg"
'''
