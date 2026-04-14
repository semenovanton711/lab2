import socket
import os


def send_file_to_server(filename, host='localhost', port=8888):
    """Отправляет файл на сервер"""

    # Проверяем существование файла
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        return

    # Подключаемся к серверу
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        # Отправляем команду PUT с именем файла
        cmd = f"PUT {os.path.basename(filename)}"
        sock.send(cmd.encode())

        # Получаем подтверждение готовности
        response = sock.recv(1024).decode().strip()
        if response != "READY":
            print(f"Ошибка: {response}")
            return

        # Отправляем размер файла
        file_size = os.path.getsize(filename)
        sock.send(f"SIZE {file_size}".encode())

        # Получаем подтверждение
        response = sock.recv(1024).decode().strip()
        if response != "READY":
            print(f"Ошибка: {response}")
            return

        # Отправляем файл
        with open(filename, 'rb') as f:
            while chunk := f.read(4096):
                sock.send(chunk)

        # Получаем результат
        result = sock.recv(1024).decode().strip()
        print(f"Результат: {result}")

    finally:
        sock.send("BYE".encode())
        sock.close()


# Использование
if __name__ == "__main__":
    # Отправляем файл "test.txt" на сервер
    send_file_to_server("test.txt")