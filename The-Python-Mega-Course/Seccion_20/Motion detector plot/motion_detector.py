import cv2, time, pandas
from datetime import datetime

video       = cv2.VideoCapture(0)
backgrond   = None
number      = 0
status_list = [None,None] #To avoid out of range exception
times       = [] #To avoid out of range exception
df          = pandas.DataFrame(columns=["Start","End"])
while True:
    check, frame =video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if backgrond is None:
        backgrond = gray
        #goes back to the beginning of the while loop
        continue

    delta_frame = cv2.absdiff(backgrond,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        #change this value for different results. Bigger number to bigger objects.
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        number+=1
        name=str(number)+".jpg"
        (x, y, w, h) = cv2.boundingRect(contour)
        #Parameters: frame, coordinate, coordinate, color, line width
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        #Uncomment the line below to save an image every time the camera detects and object
        #cv2.imwrite(name,frame)
    status_list.append(status)
    #Improve the use of the memory
    status_list = status_list[-2:]
    if(status_list[-1] == 1 and status_list[-2]==0):
        times.append(datetime.now())
    if(status_list[-1] == 0 and status_list[-2]==1):
        times.append(datetime.now())

    #cv2.imshow("Gray frame",gray)
    #cv2.imshow("Delta",delta_frame)
    cv2.imshow("threshold",thresh_frame)
    cv2.imshow("Color",frame)

    key = cv2.waitKey(1)
    #Breaking the while loop
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
print(status_list)
print(times)

for i in range(0,len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index = True)

#Exporting df to a csv file
df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows
