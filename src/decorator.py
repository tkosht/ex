#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import datetime
import functools
import traceback as tb

def get_now():
    return datetime.datetime.now().strftime("%Y/%m/%d %T")

def trace(f: callable) -> callable:
    """

    :param f: decorated function
    :return: wrapper function
    >>> fn = lambda : print("hello")
    >>> lg = trace(fn)
    >>> type(lg)
    <class 'function'>
    >>> lg.__name__
    '<lambda>'
    """
    assert callable(f)

    @functools.wraps(f)
    def tracer(*args, **kwargs) -> None:
        """
        tracer function for f
        :param args: args for the function f
        :param kwargs:kwargs for the function f
        :return:
        """
        print(f"{get_now()} Start {f.__name__} {args}")
        # print(s)   # for raise exception
        r = f(*args, **kwargs)
        print(f"{get_now()} End {f.__name__} {args}")
        return r

    return tracer

def format4logging(msg):
    assert isinstance(msg, str)
    m = re.sub(r"\n\s*", " ", msg)
    return m

def exc(f: callable) -> callable:
    """

    :param f: decorated function
    :return: wrapper function
    """
    assert callable(f)

    @functools.wraps(f)
    def exceptor(*args, **kwargs) -> None:
        try:
            f(*args, **kwargs)
        except Exception as e:
            err_info = tb.format_exc(-1, chain=e)   # - just the last stack
            #err_info = tb.format_exc(chain=e)
            err_info = format4logging(err_info)
            print(f"Caught Exception: {e} / {err_info}")
        return

    return exceptor


if __name__ == "__main__":
    pass
