import cv2
import socket
import pickle
import os
# import numpy as np


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "192.168.0.133"
server_port = 6666
s.bind((server_ip, server_port))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec

i = 0
if os.path.exists(f'output{i}.avi'):
    i += 1
output_file = f'output{i}.avi'  # Output file name

fps = 20.0  # Frames per second
frame_width = 640  # Width of the frames
frame_height = 480  # Height of the frames

out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))


while True:
    x = s.recvfrom(1000000)
    client_ip = x[1][0]
    data = x[0]
    data = pickle.loads(data)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    cv2.imshow("Img Server", img)

    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)

    # Perform Unsharp Masking
    sharpened = cv2.addWeighted(img, 7, blurred, -2, 1) #(img, alpha, blurred, beta, gamma) change alpha and beta to tweak sharpness

    cv2.imshow("fitered", sharpened)
    
    cv2.waitKey(33)  # approximately 1000ms / 30fps

    out.write(sharpened)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
