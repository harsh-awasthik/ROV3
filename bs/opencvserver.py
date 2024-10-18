import cv2
import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "192.168.0.133"
server_port = 6666
s.bind((server_ip, server_port))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
output_file = 'output.avi'  # Output file name
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

    out.write(img)

    cv2.imshow("Img Server", img)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
