#! /usr/bin/env python

import unittest
import inc_exc
#from decimal import Decimal as D

class UndefinedTests(unittest.TestCase):
    def test_n_greater_than_t(self):
        self.assertLess(inc_exc.prob_atleastonemiss(10, 5) - 1, .000001)
        
    def test_n2_t2(self):
        self.assertEqual(inc_exc.prob_atleastonemiss(2, 2), .5)

    def test_n2_t3(self):
        self.assertLess(inc_exc.prob_atleastonemiss(2, 3) - .25, .000001)

    def test_n3_t3(self):
        self.assertLess(inc_exc.prob_atleastonemiss(3, 3)-.777777777778, .000001)


if __name__ == '__main__':
    unittest.main()
