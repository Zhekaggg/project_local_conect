import socket
import pickle
import struct
import cv2

# Настройка сокета
HOST = 'IP_ОТПРАВИТЕЛЯ'  # IP отправителя (сервер)
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

data = b""
payload_size = struct.calcsize("L")

try:
    while True:
        # Получение размера сообщения
        while len(data) < payload_size:
            data += client_socket.recv(4096)
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        # Получение самого сообщения (изображения)
        while len(data) < msg_size:
            data += client_socket.recv(4096)
        
        frame_data = data[:msg_size]
        data = data[msg_size:]

        # Десериализация данных
        frame = pickle.loads(frame_data)

        # Декодирование изображения
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Отображение изображения
        cv2.imshow('Полученное видео с камеры', frame)
        if cv2.waitKey(1) == 27:  # Нажмите ESC для выхода
            break

finally:
    client_socket.close()
    cv2.destroyAllWindows()
