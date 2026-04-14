import socket, threading, os, signal, sys
from pathlib import Path


class FileServer:
    def __init__(self, host='localhost', port=8888, base_dir='./server_files'):
        self.host, self.port, self.base_dir = host, port, Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        self.running = True
        self.clients = []
        signal.signal(signal.SIGINT, self.shutdown)

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Сервер запущен на {self.host}:{self.port}")

        while self.running:
            try:
                client, addr = self.sock.accept()
                threading.Thread(target=self.handle_client, args=(client, addr), daemon=True).start()
                self.clients.append(client)
                print(f"Клиент {addr} подключился")
            except:
                pass

    def handle_client(self, client, addr):
        try:
            while True:
                data = client.recv(4096).decode().strip()
                if not data: break

                cmd = data.split()[0].upper()
                if cmd == 'LIST':
                    files = [f for f in os.listdir(self.base_dir) if (self.base_dir / f).is_file()]
                    client.send(("OK\n" + "\n".join(files)).encode())

                elif cmd == 'GET' and len(data.split()) > 1:
                    fname = data.split()[1]
                    fpath = self.base_dir / fname
                    if fpath.exists() and fpath.is_file():
                        size = fpath.stat().st_size
                        client.send(f"OK {size}".encode())
                        if client.recv(1024).decode() == 'READY':
                            with open(fpath, 'rb') as f:
                                while chunk := f.read(4096):
                                    client.send(chunk)
                            print(f"Файл {fname} отправлен")
                    else:
                        client.send(f"ERROR Файл не найден".encode())

                # НОВЫЙ БЛОК: Добавление файла на сервер
                elif cmd == 'PUT' and len(data.split()) > 1:
                    fname = data.split()[1]
                    fpath = self.base_dir / fname

                    # Подтверждаем готовность принять файл
                    client.send("READY".encode())

                    # Получаем размер файла
                    size_data = client.recv(1024).decode().strip()
                    if size_data.startswith("SIZE"):
                        file_size = int(size_data.split()[1])
                        client.send("READY".encode())

                        # Принимаем файл
                        received = 0
                        with open(fpath, 'wb') as f:
                            while received < file_size:
                                chunk = client.recv(min(4096, file_size - received))
                                if not chunk:
                                    break
                                f.write(chunk)
                                received += len(chunk)

                        print(f"Файл {fname} получен ({received} байт)")
                        client.send("OK Файл загружен".encode())
                    else:
                        client.send("ERROR Ошибка размера".encode())

                elif cmd == 'BYE':
                    break
                else:
                    client.send("ERROR Неизвестная команда".encode())
        except:
            pass
        finally:
            client.close()
            self.clients.remove(client)
            print(f"Клиент {addr} отключился")

    def shutdown(self, *args):
        print("\nЗавершение работы...")
        self.running = False
        for c in self.clients: c.close()
        self.sock.close()
        sys.exit(0)


if __name__ == "__main__":
    args = sys.argv[1:]
    FileServer(args[0] if args else 'localhost',
               int(args[1]) if len(args) > 1 else 8888,
               args[2] if len(args) > 2 else './server_files').start()