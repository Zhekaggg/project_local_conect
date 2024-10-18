from ftplib import FTP

# Подключение к FTP-серверу
ftp = FTP('192.168.1.9')  # Замените на IP-адрес вашего сервера
ftp.login(user='user', passwd='12345')

# Открытие файла для отправки
with open('C:/Users/Zheka/Desktop/Новая папка (4)/images.png', 'rb') as file:
    ftp.storbinary('STOR photo.jpg', file)

# Закрытие соединения
ftp.quit()
print("Фото отправлено успешно")
