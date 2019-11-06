import cv2, time


'''
first paramether is whether the camera number (0 webcam,1 external,2 external...)
or a file name (movie.mp4)
Once we execute this line, our led camera will turn on for a second. Just that
'''
video = cv2.VideoCapture(0)



'''
To take a frame what is watching the camera.
img = cv2.imwrite("photo.jpg",frame)
'''
#total frames
a=0
while True:
    check, frame =video.read()
    cv2.imshow("Capturing",frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing",gray)
    a+=1
    key = cv2.waitKey(1)
    #Breaking the while loop
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows
