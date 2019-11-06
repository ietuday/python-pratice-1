import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("me.jpg")
#Images are read in gray scale to detect features in a better format

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
print(type(faces))
print(faces)
# scaleFactor = 1.05 decreases scaleFactor by 5%
# faces holds the x, y, width, height values of the face detected

for x,y,width,height in faces:
    mg=cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),3)
resized_img= cv2.resize(img,(int(gray_img.shape[1]/3),int(gray_img.shape[0]/3)))
cv2.imshow("Face",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
