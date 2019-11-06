import cv2, time
# Combining the Face_detection and Video_Capturing Code
video = cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=3)
    for x,y,width,height in faces:
        mg=cv2.rectangle(gray_img,(x,y),(x+width,y+height),(0,255,0),3)
    cv2.imshow("Capturing", gray_img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(frames_counter)
video.release()

cv2.destroyAllWindows()
