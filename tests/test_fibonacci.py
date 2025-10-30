import unittest
from fibonacci import fib_iterative, fib_recursive, fib_memo, fib_sequence


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.expected = [0, 1, 1, 2, 3, 5, 8, 13]

    def test_iterative_small(self):
        for i, val in enumerate(self.expected):
            self.assertEqual(fib_iterative(i), val)

    def test_recursive_small(self):
        # 朴素递归对小 n 应该正确
        for i, val in enumerate(self.expected):
            self.assertEqual(fib_recursive(i), val)

    def test_memo_small(self):
        for i, val in enumerate(self.expected):
            self.assertEqual(fib_memo(i), val)

    def test_sequence(self):
        self.assertEqual(list(fib_sequence(len(self.expected))), self.expected)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib_iterative(-1)
        with self.assertRaises(ValueError):
            fib_recursive(-2)
        with self.assertRaises(ValueError):
            fib_memo(-10)

    def test_consistency_large(self):
        # 对于较大的 n，迭代与记忆化应一致
        n = 30
        self.assertEqual(fib_iterative(n), fib_memo(n))


if __name__ == "__main__":
    unittest.main()
