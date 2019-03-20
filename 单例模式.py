# -*- coding: utf8 -*-
class Singleton:
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    pass