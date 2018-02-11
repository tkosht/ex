# coding:utf-8

from ex import Ex

def test_ex1():
    _msg="abc"
    ex = Ex(msg=_msg)
    m = ex.get_msg()
    assert m == _msg

def test_ex2():
    _msg="abc"
    ex = Ex(msg=_msg)
    h = ex.hello()
    assert h == "hello and %s" % (_msg)

