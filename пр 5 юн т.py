import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Импортируем функцию из вашего файла
from пр5РЕКУРС import solve_recursive

class TestSolveRecursive(unittest.TestCase):

    def setUp(self):
        """Подготовка к каждому тесту: сохраняем stdout для имитации"""
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """Восстановление stdout после теста"""
        sys.stdout = self.held

    # Тест 1: базовый случай — полностью известный массив
    @patch('sys.stdin', StringIO('1\n1\n1\n'))
    def test_known_array_single_element(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            self.assertIn('Количество валидных массивов: 1', output)

    # Тест 2: один неизвестный элемент (0)
    @patch('sys.stdin', StringIO('1\n2\n0\n'))
    def test_unknown_element(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            # Ожидаем 2 варианта: 1 или 2 (так как m=2, и разница <=1)
            self.assertIn('Количество валидных массивов: 2', output)

    # Тест 3: массив с несколькими неизвестными элементами
    @patch('sys.stdin', StringIO('2\n2\n0\n0\n'))
    def test_multiple_unknowns(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            # Для двух позиций с 0 и m=2: (1,1), (1,2), (2,1), (2,2) — 4 варианта
            self.assertIn('Количество валидных массивов: 4', output)

    # Тест 4: последовательность с известными элементами (проверка логики разницы <=1)
    @patch('sys.stdin', StringIO('3\n3\n1\n2\n3\n'))
    def test_valid_sequence(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            self.assertIn('Количество валидных массивов: 1', output)

    # Тест 5: последовательность с нарушением условия (должна дать 0 вариантов)
    @patch('sys.stdin', StringIO('2\n3\n1\n3\n'))
    def test_invalid_sequence(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            self.assertIn('Количество валидных массивов: 0', output)

    # Тест 6: проверка обработки ошибок ввода (пустой ввод)
    @patch('sys.stdin', StringIO('\n1\n1\n1\n'))
    def test_empty_input(self):
        with self.assertRaises(ValueError) as context:
            solve_recursive()
        self.assertIn('Пустой ввод', str(context.exception))

    # Тест 7: проверка обработки ошибок (выход за пределы max_val)
    @patch('sys.stdin', StringIO('1\n1\n2\n'))
    def test_exceed_max_value(self):
        with self.assertRaises(ValueError) as context:
            solve_recursive()
        self.assertIn('Значение должно быть <= 1', str(context.exception))

    # Тест 8: граничные значения (максимальный n и m)
    @patch('sys.stdin', StringIO('3\n100\n0\n0\n0\n'))
    def test_boundary_values(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve_recursive()
            output = mock_stdout.getvalue().strip()
            result = int(output.split()[-1])  # Извлекаем число из строки
            self.assertGreaterEqual(result, 0)
            self.assertLess(result, 10**9 + 7)  # Проверяем MOD

    # Тест 9: прерывание пользователем (KeyboardInterrupt)
    @patch('sys.stdin', StringIO('1\n1\n1\n'))
    def test_keyboard_interrupt(self):
        with patch('sys.stdin.readline', side_effect=KeyboardInterrupt):
            result = solve_recursive()
            self.assertEqual(result, 1)  # Функция должна вернуть 1 при прерывании


if __name__ == '__main__':
    unittest.main()
