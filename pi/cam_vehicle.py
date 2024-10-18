import cv2
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000000)

server_ip = "192.168.0.133" # IP of server
server_port = 6666

cap = cv2.VideoCapture(0)
cap.set(3, 640) # Set width
cap.set(4, 480) # Set height

while True:
    ret, img = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])

    x_as_bytes = pickle.dumps(buffer)
    s.sendto((x_as_bytes), (server_ip, server_port))

    cv2.imshow("Video", img) # Comment it for smoother functioning

    if cv2.waitKey(1) & 0xFF == ord("q"): # Press Ctrl+q to exit.
        break

cv2.destroyAllWindows()
cap.release()
