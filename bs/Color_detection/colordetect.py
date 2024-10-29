import numpy as np
import cv2

# cap = cv2.VideoCapture(0)

while True:
    # ret, frame = cap.read()
    img = cv2.imread(f"img2.jpg")
    # scale = 0.75
    # img = cv2.resize(frame, None, fx=scale, fy=scale)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([50, 0, 0])
    upper = np.array([130, 255, 255])
    mask_not = cv2.inRange(hsv, lower, upper)
    cv2.imshow("mask_not", mask_not)

    mask= cv2.bitwise_not(mask_not)
    # cv2.imshow("mask", mask)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("detected", result)
    cv2.imshow("Original Video", img)

    if cv2.waitKey(1) == ord('q'):
        break

img.release()
cv2.destroyAllWindows()