#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# person.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def jump(self):
        print("jump", self)

    def fly(self):
        self.jump()
        print("fly")


def intro_func(self, content):
    print("intro, message, {}".format(content))


a = Person("Todd", 35)


def intro_func(self, content):
    print("intro function {}".format(content))


from types import MethodType
a.intro = MethodType(intro_func, a)
a.intro("my_func")
