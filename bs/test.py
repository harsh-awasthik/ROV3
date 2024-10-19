import cv2

vid = cv2.VideoCapture(2)


while True:
    ret, img = vid.read()
    cv2.imshow("Img Server", img)

    # Apply Gaussian blur to create the blurred version
    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)

    # Perform Unsharp Masking
    sharpened = cv2.addWeighted(img, 7, blurred, -2, 1) #(img, alpha, blurred, beta, gamma) change alpha and beta to tweak sharpness

    cv2.imshow("fitered", sharpened)
    
    cv2.waitKey(33)  # approximately 1000ms / 30fps

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
