import unittest

def recurs_sequence(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n должно быть натуральным числом")
    if n == 1:
        return -3
    return 2 * recurs_sequence(n - 1) + 5

class TestSequenceFunctions(unittest.TestCase):
    def test_recurs(self):
        self.assertEqual(recurs_sequence(1), -3)
        self.assertEqual(recurs_sequence(2), -1)
        self.assertEqual(recurs_sequence(3), 3)
        self.assertEqual(recurs_sequence(4), 11)
        self.assertEqual(recurs_sequence(5), 27)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            recurs_sequence(0)
        with self.assertRaises(ValueError):
            recurs_sequence(-5)
        with self.assertRaises(ValueError):
            recurs_sequence("abc")

if __name__ == "__main__":
    unittest.main()