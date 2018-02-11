#!/usr/bin/env python

def f(x):
    if x == 1:
        return 1
    return x*f(x-1)
def test_answer():
    assert f(3) == 6
