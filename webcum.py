import socket
import cv2
import pickle
import struct

# Настройка сокета
HOST = '0.0.0.0'  # IP отправителя
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Ожидание подключения клиента...')
conn, addr = server_socket.accept()
print(f'Подключен: {addr}')

# Захват видео с камеры
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Сжатие изображения убрано
        frame = cv2.resize(frame, (640, 480))

        # Сериализация данных с использованием pickle
        data = pickle.dumps(frame)
        message_size = struct.pack("L", len(data))

        # Отправка размера сообщения и самого сообщения
        conn.sendall(message_size + data)

finally:
    cap.release()
    conn.close()
    server_socket.close()