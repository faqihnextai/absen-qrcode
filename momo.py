import cv2
import time

cam_index = 0  # ganti sesuai yang ke-detect

for _ in range(5):  # coba 5x
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)
    time.sleep(1)
    if cap.isOpened():
        print("Camera is awake!")
        break
    cap.release()
else:
    print("Camera failed to activate.")

ret, frame = cap.read()
if ret:
    cv2.imshow("Webcam Logitech", frame)
    cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
# print("Camera is awake!")