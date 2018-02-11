#!/usr/bin/env python
# coding utf-8

class Ex:
    def __init__(self, msg):
        self.msg = msg
    def hello(self):
        return "hello and {}".format(msg)
    def get_msg(self):
        return self.msg

