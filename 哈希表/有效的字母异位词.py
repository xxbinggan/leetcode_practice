# 作者:lixy
# 2026年11月16日16时39分41秒
# 2695016411@qq.com
class Solution:
    def isAnagram(self,s,t):
        record=[0]*26
        for i in s:
            record[ord(i)-ord("a")]+=1
        for i in t:
            record[ord(i)-ord("a")]-=1
        for i in range(26):
            if record[i]!=0:
                return False
        return True