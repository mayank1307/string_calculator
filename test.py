import unittest
import index as calculator

class Test(unittest.TestCase):
    def test_with_no_numbers(self):
        self.assertEqual(calculator.add(''), 0)

    def test_with_single_number(self):
        self.assertEqual(calculator.add('1'), 1)
        self.assertEqual(calculator.add('5'), 5)
        self.assertEqual(calculator.add('12'), 12)
        self.assertEqual(calculator.add('122321'), 122321)

    def test_with_multiple_numbers(self):
        self.assertEqual(calculator.add('1,2'), 3)
        self.assertEqual(calculator.add('1,2,4'), 7)
        self.assertEqual(calculator.add('5,0,3'), 8)
        self.assertEqual(calculator.add('9,11,12'), 32)
        self.assertEqual(calculator.add('0,0,0'), 0)


if __name__ == '__main__':
    unittest.main()