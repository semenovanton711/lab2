import unittest
from пр7 import find_min_cubes_sum
class TestCubesSum(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(find_min_cubes_sum(1), 1)  # 1 = 1³
        self.assertEqual(find_min_cubes_sum(8), 1)  # 8 = 2³
        self.assertEqual(find_min_cubes_sum(9), 2)  # 9 = 1³ + 2³е
    def test_medium_cases(self):
        self.assertEqual(find_min_cubes_sum(28), 2)  # 28 = 3³ + 1³
        self.assertEqual(find_min_cubes_sum(17), 3)  # комбинация кубов
    def test_edge_cases(self):
        self.assertEqual(find_min_cubes_sum(0), 0)  # сумма 0 — 0 слагаемых
        self.assertEqual(find_min_cubes_sum(2), 2)  # 2 = 1³ + 1³
    def test_large_number(self):
        result = find_min_cubes_sum(100)
        self.assertGreater(result, 0)  # должно вернуть число > 0
if __name__ == '__main__':
    unittest.main()
