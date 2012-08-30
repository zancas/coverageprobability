#! /usr/bin/env python

import unittest
import inc_exc
from decimal import Decimal as D

class UndefinedTests(unittest.TestCase):
    def test_t_less_than_n(self):
        self.assertEqual(inc_exc.probofunion_inc_exc(D(10), D(5)), D(1))
        

if __name__ == '__main__':
    unittest.main()
