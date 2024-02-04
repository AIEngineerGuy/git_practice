import cv2
import time
video_path = r"C:\Users\Ajay\Videos\503.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("video",frame)
        k=cv2.waitKey(43)
        if k== ord("q"):
            break
        #time.sleep(1/30)
    else:
        break 

cv2.destroyAllWindows()