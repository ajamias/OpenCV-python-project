import cv2 as cv

# get webcam access
cv.namedWindow("webcam")
vc = cv.VideoCapture(0)

# train the model
haar_cascade = cv.CascadeClassifier("faces.xml")

if vc.isOpened():
    read_success, frame = vc.read()
else:
    read_success = False

while read_success:

    # convert frame to greyscale
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect and draw a red rectangle over all detected faces
    faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), thickness=2)

    # display modified frame
    cv.imshow("webcam", frame)

    # obtain next frame from webcam
    read_success, frame = vc.read()

    # exit on ESC
    if cv.waitKey(20) == 27:
        break

# disable webcam and remove all windows
vc.release()
cv.destroyWindow("webcam")