"""
Вариант 13
Дана последовательность действительных чисел a1→a2→...→an.
Сформируйте стек такой же размерности по следующему правилу:
элемент стека является максимальным из элементов исходного списка с номерами от 1 до k.
"""


# Класс стека
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def show(self):
        if self.items:
            print("Стек (верх -> низ):", self.items[::-1])
        else:
            print("Стек пуст")


# Класс очереди
class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            return self.items.pop(0)
        return None

    def show(self):
        if self.items:
            print("Очередь (перед -> зад):", self.items)
        else:
            print("Очередь пуста")


# Класс дека
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_back(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_back(self):
        if self.items:
            return self.items.pop()
        return None

    def show(self):
        if self.items:
            print("Дек (перед -> зад):", self.items)
        else:
            print("Дек пуст")


# Основная функция
def main():
    print("=== Программа для варианта 13 ===")

    # Ввод данных
    try:
        n = int(input("Сколько чисел в последовательности? "))
        if n <= 0:
            print("Число должно быть больше 0")
            return

        numbers = []
        print("Введите числа:")
        for i in range(n):
            num = float(input(f"a{i + 1}: "))
            numbers.append(num)

        print(f"\nИсходные числа: {numbers}")

        # 1. Создаем стек по правилу
        print("\n--- 1. Создание стека ---")
        stack = Stack()
        for k in range(1, n + 1):
            max_num = max(numbers[:k])
            stack.push(max_num)

        print("Стек создан по правилу:")
        stack.show()

        # 2. Меню для работы со стеком
        while True:
            print("\n--- Меню стека ---")
            print("1. Добавить число")
            print("2. Удалить число (с вершины)")
            print("3. Показать вершину")
            print("4. Показать весь стек")
            print("5. Перейти к очереди")

            choice = input("Ваш выбор (1-5): ")

            if choice == '1':
                num = float(input("Введите число: "))
                stack.push(num)
                print(f"Число {num} добавлено")

            elif choice == '2':
                removed = stack.pop()
                if removed is not None:
                    print(f"Удалено число: {removed}")
                else:
                    print("Стек пуст")

            elif choice == '3':
                top = stack.peek()
                if top is not None:
                    print(f"Вершина стека: {top}")
                else:
                    print("Стек пуст")

            elif choice == '4':
                stack.show()

            elif choice == '5':
                break

            else:
                print("Неверный выбор")

        # 3. Преобразуем стек в очередь
        print("\n--- 2. Преобразование в очередь ---")
        queue = Queue()

        # Копируем элементы из стека в очередь
        temp = []
        while stack.size() > 0:
            temp.append(stack.pop())

        # Восстанавливаем стек
        for item in temp[::-1]:
            stack.push(item)

        # Заполняем очередь
        for item in temp:
            queue.add(item)

        print("Очередь создана:")
        queue.show()

        # Меню для работы с очередью
        while True:
            print("\n--- Меню очереди ---")
            print("1. Добавить число")
            print("2. Удалить число (из начала)")
            print("3. Показать очередь")
            print("4. Перейти к дека")

            choice = input("Ваш выбор (1-4): ")

            if choice == '1':
                num = float(input("Введите число: "))
                queue.add(num)
                print(f"Число {num} добавлено")

            elif choice == '2':
                removed = queue.remove()
                if removed is not None:
                    print(f"Удалено число: {removed}")
                else:
                    print("Очередь пуста")

            elif choice == '3':
                queue.show()

            elif choice == '4':
                break

            else:
                print("Неверный выбор")

        # 4. Преобразуем стек в дек
        print("\n--- 3. Преобразование в дек ---")
        deque = Deque()

        # Заполняем дек элементами из стека
        temp = []
        while stack.size() > 0:
            temp.append(stack.pop())

        # Восстанавливаем стек
        for item in temp[::-1]:
            stack.push(item)

        # Заполняем дек
        for item in temp:
            deque.add_back(item)

        print("Дек создан:")
        deque.show()

        # Меню для работы с деком
        while True:
            print("\n--- Меню дека ---")
            print("1. Добавить в начало")
            print("2. Добавить в конец")
            print("3. Удалить из начала")
            print("4. Удалить из конца")
            print("5. Показать дек")
            print("6. Выход")

            choice = input("Ваш выбор (1-6): ")

            if choice == '1':
                num = float(input("Введите число: "))
                deque.add_front(num)
                print(f"Число {num} добавлено в начало")

            elif choice == '2':
                num = float(input("Введите число: "))
                deque.add_back(num)
                print(f"Число {num} добавлено в конец")

            elif choice == '3':
                removed = deque.remove_front()
                if removed is not None:
                    print(f"Удалено из начала: {removed}")
                else:
                    print("Дек пуст")

            elif choice == '4':
                removed = deque.remove_back()
                if removed is not None:
                    print(f"Удалено из конца: {removed}")
                else:
                    print("Дек пуст")

            elif choice == '5':
                deque.show()

            elif choice == '6':
                print("\n=== Программа завершена ===")
                return

            else:
                print("Неверный выбор")

    except ValueError:
        print("Ошибка: введите правильное число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()