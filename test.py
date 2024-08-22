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

    def test_with_newline(self):
        self.assertEqual(calculator.add('1\n2'), 3)
        self.assertEqual(calculator.add('1\n2,4'), 7)
        self.assertEqual(calculator.add('5,0\n3'), 8)
        self.assertEqual(calculator.add('9\n11\n12,9\n11\n12,9\n11\n12,9\n11\n12'), 128)
        self.assertEqual(calculator.add('0,0\n0'), 0)

    def test_with_custom_delimiters(self):
        self.assertEqual(calculator.add( "//;\n1;2" ), 3)
        self.assertEqual(calculator.add( "//;\n1;2;3;4;5" ), 15)
        self.assertEqual(calculator.add( "//;\n1" ), 1)
        self.assertEqual(calculator.add( "//;\n0" ), 0)
        self.assertEqual(calculator.add( "//;\n" ), 0)

    def test_negatives(self):
        tests = [
            ('-1', 'Negative numbers not allowed: [-1]'),
            ('-1\n-2,4', 'Negative numbers not allowed: [-1, -2]'),
            ('//;\n-1;2;-3;4;-5', 'Negative numbers not allowed: [-1, -3, -5]')
        ]
        for test, error in tests:
            with self.assertRaises(ValueError) as context:
                calculator.add(test)
            self.assertEqual(str(context.exception), error)

if __name__ == '__main__':
    unittest.main()