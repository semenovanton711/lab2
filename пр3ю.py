import unittest


def find_peak_hour(n, passengers, k):
    """
    Функция для поиска максимальной суммы k подряд идущих элементов
    """
    max_sum = 0
    for i in range(n - k + 1):
        current_sum = sum(passengers[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


class TestPeakHour(unittest.TestCase):

    def test_example_from_task(self):
        """Тест из условия задачи"""
        result = find_peak_hour(7, [3, 2, 5, 4, 3, 2, 4], 3)
        self.assertEqual(result, 12)

    def test_single_element(self):
        """Один элемент"""
        result = find_peak_hour(1, [5], 1)
        self.assertEqual(result, 5)

    def test_all_same_numbers(self):
        """Все числа одинаковые"""
        result = find_peak_hour(4, [2, 2, 2, 2], 2)
        self.assertEqual(result, 4)

    def test_peak_at_beginning(self):
        """Максимальная сумма в начале"""
        result = find_peak_hour(5, [10, 8, 3, 2, 1], 2)
        self.assertEqual(result, 18)

    def test_peak_at_end(self):
        """Максимальная сумма в конце"""
        result = find_peak_hour(5, [1, 2, 3, 8, 10], 2)
        self.assertEqual(result, 18)

    def test_k_equals_n(self):
        """k равно n (вся последовательность)"""
        result = find_peak_hour(3, [1, 2, 3], 3)
        self.assertEqual(result, 6)

    def test_minimal_values(self):
        """Минимальные значения"""
        result = find_peak_hour(2, [1, 1], 1)
        self.assertEqual(result, 1)

    def test_large_numbers(self):
        """Большие числа"""
        result = find_peak_hour(4, [100, 200, 150, 300], 2)
        self.assertEqual(result, 450)

    def test_zeros(self):
        """Все нули"""
        result = find_peak_hour(3, [0, 0, 0], 2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    # Запуск тестов
    unittest.main()