# -*- coding: utf8 -*-
def insertion_sort(_list):
    n = len(_list)
    for i in range(1, n):
        value = _list[i]
        pos = i
        while pos > 0 and value < _list[pos - 1]:
            _list[pos] = _list[pos - 1]
            pos -= 1
        _list[pos] = value