# -*- coding: utf8 -*-
def test(list1):
    if not list1:
        return ""


    base = list1[0]
    if len(list1) == 1:
        return base
    if not base:
        return ""
    public_index = 1
    while public_index < len(base):
        public = base[0:public_index]
        for i in list1:
            if not i.startswith(public):
                if not public[0:-1]:
                    return "1"
                return public[0:-1]
            else:
                pass
        public_index = public_index + 1

a = test( ["a","b","c"])
print(a)