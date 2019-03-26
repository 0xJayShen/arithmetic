# -*- coding: utf8 -*-
def catalan(n):
    if n==0 or n==1:
        return 1
    return ((4*n-2)*catalan(n-1))/(n+1)
res = catalan(6)
print(res)
