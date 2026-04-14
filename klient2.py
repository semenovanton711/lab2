import socket, sys
from pathlib import Path


class FileClient:
    def __init__(self, host='localhost', port=8888):
        self.host, self.port = host, port
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            print(f"Подключен к {self.host}:{self.port}")
            return True
        except:
            print("Ошибка подключения")
            return False

    def list_files(self):
        self.sock.send("LIST".encode())
        resp = self.sock.recv(4096).decode()
        if resp.startswith('OK'):
            files = resp[3:].strip()
            print("\nФайлы на сервере:")
            print(files if files else "  Пусто")
        else:
            print("Ошибка")

    def download(self, filename, save_dir='./downloads'):
        Path(save_dir).mkdir(exist_ok=True)
        self.sock.send(f"GET {filename}".encode())
        resp = self.sock.recv(1024).decode()

        if resp.startswith('OK'):
            size = int(resp.split()[1])
            self.sock.send("READY".encode())

            path = Path(save_dir) / filename
            with open(path, 'wb') as f:
                recv = 0
                while recv < size:
                    data = self.sock.recv(min(4096, size - recv))
                    if not data: break
                    f.write(data)
                    recv += len(data)
                    print(f"\rЗагружено: {recv / size * 100:.1f}%", end='')
            print(f"\nФайл сохранен в {path}")
        else:
            print(f"Ошибка: {resp[6:]}")

    def run(self):
        if not self.connect(): return
        print("Команды: list, get <файл>, quit")

        while True:
            try:
                cmd = input("\n> ").strip().lower()
                if cmd == 'quit':
                    self.sock.send("BYE".encode())
                    break
                elif cmd == 'list':
                    self.list_files()
                elif cmd.startswith('get '):
                    self.download(cmd[4:])
                elif cmd:
                    print("? list/get/quit")
            except:
                print("Соединение потеряно")
                break
        self.sock.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    FileClient(args[0] if args else 'localhost',
               int(args[1]) if len(args) > 1 else 8888).run()get