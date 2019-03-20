# -*- coding: utf8 -*-
def rev_str(my_str):
    old_list = list(my_str)
    print(old_list)
    new_str = ""
    while len(old_list)>0:
        new_str = new_str + (old_list.pop())
    print(new_str)
rev_str("12344555")