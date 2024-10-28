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


# def adjust_gamma(image, gamma=1.0):
#     invGamma = 1.0 / gamma
#     table = np.array([(i / 255.0) ** invGamma * 255 for i in np.arange(0, 256)]).astype("uint8")
#     return cv2.LUT(image, table)


while True:
    x = s.recvfrom(1000000)
    client_ip = x[1][0]
    data = x[0]
    data = pickle.loads(data)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)

    out.write(img)

    cv2.imshow("Img Server", img)

    # Use gamma < 1 to brighten
    # adjusted = adjust_gamma(img, gamma=0.5)
    # filtered = cv2.bilateralFilter(adjusted, 9, 75, 75)
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    # for i in range(3):  # Apply CLAHE to each color channel
    #     img[:,:,i] = clahe.apply(img[:,:,i])

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
