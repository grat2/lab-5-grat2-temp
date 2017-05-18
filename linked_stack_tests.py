import unittest
from linked_stack import *
from linked_list import *

class TestCase(unittest.TestCase):
    def test_class(self):
        s1 = Stack(Pair(5, Pair(10, Pair(15, None))))
        self.assertEqual(s1.l, Pair(5, Pair(10, Pair(15, None))))
        self.assertEqual(repr(s1), "Stack({!r})".format(Pair(5, Pair(10, Pair(15, None)))))
        s2 = Stack(Pair(5, Pair(10, Pair(15, None))))
        self.assertEqual(s1, s2)

    def test_empty_stack(self):
        self.assertEqual(empty_stack(), Stack(empty_list()))

    def test_push(self):
        s1 = Stack(Pair(5, Pair(10, Pair(15, None))))
        s2 = Stack(Pair(5, Pair(10, Pair(15, Pair(20, None)))))
        self.assertEqual(push(s1, 20), s2)
        s3 = empty_stack()
        s4 = Stack(Pair(21, None))
        self.assertEqual(push(s3, 21), s4)
        s5 = Stack(Pair(1, Pair(2, None)))
        s6 = Stack(Pair(1, Pair(2, Pair(3, None))))
        self.assertEqual(push(s5, 3), s6)

    def test_pop(self):
        s1 = Stack(Pair(5, Pair(10, Pair(15, None))))
        s2 = Stack(Pair(5, Pair(10, None)))
        self.assertEqual(pop(s1), (15, s2))
        s3 = empty_stack()
        self.assertRaises(IndexError, pop, s3)
        s4 = Stack(Pair(21, None))
        s5 = Stack(empty_list())
        self.assertEqual(pop(s4), (21, s5))

    def test_peek(self):
        s1 = Stack(Pair(5, Pair(10, Pair(15, None))))
        self.assertEqual(peek(s1), 15)
        s2 = Stack(Pair(12, None))
        self.assertEqual(peek(s2), 12)
        s3 = empty_stack()
        self.assertRaises(IndexError, peek, s3)

    def test_size(self):
        s1 = empty_stack()
        self.assertEqual(size(s1), 0)
        s2 = Stack(Pair(1, Pair(2, Pair(43, Pair(44, None)))))
        self.assertEqual(size(s2), 4)

    def test_is_empty(self):
        s1 = empty_stack()
        self.assertEqual(is_empty(s1), True)
        s2 = Stack(Pair(1, None))
        self.assertEqual(is_empty(s2), False)

if(__name__ == "__main__"):
    unittest.main()
