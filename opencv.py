import cv2 as cv

cv.namedWindow("webcam")
vc = cv.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv.imshow("webcam", frame)
    rval, frame = vc.read()
    key = cv.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv.destroyWindow("webcam")