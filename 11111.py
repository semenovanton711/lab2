import unittest
import first
class CalcTest(unittest.TestCase):
    def t1(self):
        self.assertEqual(first.y(1,2),3)
    def t2(self):
        self.assertEqual(first.y(2, 1), 3)
    def t3(self):
        self.assertEqual(first.y(1, 1), 0)
    def t4(self):
        self.assertEqual(first.y(2, 2), 0)
    def t5(self):
        self.assertEqual(first.y(2, 3), 5)
    def t6(self):
        self.assertEqual(first.y(3, 2), 5)


#точка ввода командной строки
if __name__=='__main__':
    unittest.main()