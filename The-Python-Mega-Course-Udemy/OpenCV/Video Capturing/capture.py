import cv2, time

frames_counter = 0
video = cv2.VideoCapture(0) # 0 -> 1 video camera
# When we put in a number as the argument, we are using it to capture from a camera
while True:
    frames_counter = frames_counter + 1
    check, frame = video.read() # Looping is done through this frame variable

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(frames_counter)
video.release()

cv2.destroyAllWindows()
