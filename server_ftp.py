from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Создание авторизатора
authorizer = DummyAuthorizer()

# Добавление пользователя с правами на чтение и запись
authorizer.add_user("user", "12345", "/path/to/your/directory", perm="elradfmwMT")

# Создание обработчика FTP
handler = FTPHandler
handler.authorizer = authorizer

# Настройка FTP-сервера
server = FTPServer(("0.0.0.0", 21), handler)

# Запуск сервера
print("FTP-сервер запущен на порту 21")
server.serve_forever() 
