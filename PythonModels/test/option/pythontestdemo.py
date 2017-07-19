# -*- coding: utf-8 -*-
"""
Created by hushiwei on 16-12-22.
"""

import unittest

class testhello(unittest.TestCase):
    def test_hello(self):
        a={'a':1}
        self.assertEquals(a['a'],1)