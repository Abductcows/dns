import unittest

from src.utils import select_bits


class MyTestCase(unittest.TestCase):
    def test_cases(self):
        return [
            '00000000',
            '00000001',
            '10000000',
            '10000001',
            '01010101',
            '10101010',
            '11111111',
            '11011010'
        ]

    def test_bit_slicing(self):
        numbers = self.test_cases()
        for num_str in numbers:
            num = int(num_str, 2)
            for start in range(0, len(num_str) - 1):
                for length in range(1, len(num_str) - start):
                    expected = int(num_str[start: start + length], 2)
                    result = select_bits(num, len(num_str), start, length)
                    try:
                        self.assertEqual(expected, result)
                    except AssertionError:
                        print(f'fail\n{num_str=}\n{start=}\n{length=}')
                        raise


if __name__ == '__main__':
    unittest.main()
