# coding:utf-8

import unittest
from fuga import Fuga

class ExTest(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def test_first(self):
        print('test_first')
    def test_ex1(self):
        _msg="abc"
        ex = Ex(msg=_msg)
        m = ex.get_msg()
        self.assertTrue(m == _msg)
    def test_ex2(self):
        _msg="abc"
        ex = Ex(msg=_msg)
        h = ex.hello()
        self.assertTrue(m == "hello and %s" % (_msg))

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(ExTest))
    return suite

