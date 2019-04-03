# -*- coding: utf8 -*-
# https://www.cnblogs.com/zzqit/p/10045607.html
def lengthOfLongestSubstring( s):
    # 找到重复值时，更新start的值，为什么使用max，因为start有可能大于dic[s[end]] + 1，
    # 比如当s = 'abba'，end走到最后的时候，上一次start因为b做了更新变为了2。
    ans = start = 0
    pos = {}    # last index of element
    for end, c in enumerate(s):
        if c in pos:
            start = max(start, pos[c]+1)
        pos[c] = end
        ans = max(ans, end-start+1)
    print(ans)
    return ans

lengthOfLongestSubstring("ddfafaefdsfdfewrqewaddddd")