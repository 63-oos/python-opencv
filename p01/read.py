import cv2 as cv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR,'..','image','messi.jpg')
video_path = os.path.join(BASE_DIR,'..','image','test.mp4')

img = cv.imread(img_path)
if img is None:
    print("failed to load the image...")

cv.imshow('messi',img)

cv.waitKey(0)
cv.destroyAllWindows()
video = cv.VideoCapture(video_path)

while True:
    isTrue,frame = video.read()


    if not isTrue:
        video.set(cv.CAP_PROP_POS_FRAMES,0)
        continue

    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()