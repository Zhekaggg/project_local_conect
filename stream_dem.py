import socket
import pyautogui
import pickle
import struct
import cv2
import numpy as np

# Настройка сокета
HOST = '0.0.0.0'  # IP отправителя
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Ожидание подключения клиента...')
conn, addr = server_socket.accept()
print(f'Подключен: {addr}')

try:
    while True:
        # Захват экрана
        screen = pyautogui.screenshot()

        # Преобразование скриншота в numpy массив
        frame = np.array(screen)

        # Сжатие изображения для уменьшения трафика
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame)

        # Сериализация данных и отправка
        data = pickle.dumps(buffer)
        message_size = struct.pack("L", len(data))

        # Отправка размера сообщения и самого сообщения
        conn.sendall(message_size + data)

finally:
    conn.close()
    server_socket.close()
