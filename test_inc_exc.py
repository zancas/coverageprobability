#! /usr/bin/env python

import unittest
import inc_exc
from decimal import Decimal as D

class UndefinedTests(unittest.TestCase):
    def test_n_greater_than_t(self):
        self.assertEqual(inc_exc.prob_atleastonemiss(D(10), D(5)), D(1))
        
    def test_n2_t2(self):
        self.assertEqual(inc_exc.prob_atleastonemiss(D(2), D(2)), D(.5))

    def test_n2_t3(self):
        self.assertEqual(inc_exc.prob_atleastonemiss(D(2), D(3)), D(.25))

    def test_n3_t3(self):
        self.assertLess(inc_exc.prob_atleastonemiss(D('3.00000000'), D('3.00000000'))-D(.7777777777777777778), .000001)


if __name__ == '__main__':
    unittest.main()
