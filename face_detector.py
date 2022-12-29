import cv2 as cv

# get webcam access
vc = cv.VideoCapture(0)

# train the model
haar_cascade = cv.CascadeClassifier("faces.xml")

while True:

    # obtain next frame from webcam
    read_success, frame = vc.read()

    # exit on ESC
    if cv.waitKey(20) == 27 or not read_success:
        break

    # convert frame to greyscale
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect and draw a pink rectangle over all detected faces
    faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (147,20,255), thickness=2)
        cv.putText(frame, "cutie", (x, y+h-10), cv.FONT_HERSHEY_SIMPLEX, w/200, (147,20,255), thickness=2)

    # display modified frame
    cv.imshow("webcam", frame)

# disable webcam and remove all windows
vc.release()
cv.destroyAllWindows()