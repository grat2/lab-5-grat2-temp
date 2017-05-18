import unittest
from array_stack import *
from array_list import *

class TestCase(unittest.TestCase):
    def test_class(self):
        s1 = Stack(List([5, 10, 15], 3, 3))
        self.assertEqual(s1.l, List([5, 10, 15], 3, 3))
        self.assertEqual(repr(s1), "Stack({!r})".format(List([5, 10, 15], 3, 3)))
        s2 = Stack(List([5, 10, 15], 3, 3))
        self.assertEqual(s1, s2)

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack(empty_list()))

    def test_push(self):
        s1 = Stack(List([5, 10, 15, None, None], 5, 3))
        s2 = Stack(List([5, 10, 15, 20, None], 5, 4))
        self.assertEqual(push(s1, 20), s2)
        s3 = empty_stack()
        s4 = Stack(List([21], 1, 1))
        self.assertEqual(push(s3, 21), s4)
        s5 = Stack(List([1, 2, None], 3, 2))
        s6 = Stack(List([1, 2, 3], 3, 3))
        self.assertEqual(push(s5, 3), s6)

    def test_pop(self):
        s1 = Stack(List([5, 10, 15, None, None], 5, 3))
        s2 = Stack(List([5, 10, None, None, None], 5, 2))
        self.assertEqual(pop(s1), (15, s2))
        s3 = empty_stack()
        self.assertRaises(IndexError, pop, s3)
        s4 = Stack(List([21], 1, 1))
        s5 = Stack(List([None], 1, 0))
        self.assertEqual(pop(s4), (21, s5))

    def test_peek(self):
        s1 = Stack(List([5, 10 ,15, None, None], 5, 3))
        self.assertEqual(peek(s1), 15)
        s2 = Stack(List([12, None], 2, 1))
        self.assertEqual(peek(s2), 12)
        s3 = empty_stack()
        self.assertRaises(IndexError, peek, s3)

    def test_size(self):
        s1 = empty_stack()
        self.assertEqual(size(s1), 0)
        s2 = Stack(List([1, 2, 43, 44, None, None, None], 7, 4))
        self.assertEqual(size(s2), 4)

    def test_is_empty(self):
        s1 = empty_stack()
        self.assertEqual(is_empty(s1), True)
        s2 = Stack(List([1], 1, 1))
        self.assertEqual(is_empty(s2), False)

if(__name__ == "__main__"):
    unittest.main()
