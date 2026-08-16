# 作者:lixy
# 2026年08月16日22时30分19秒
# 2695016411@qq.com
class Solution:
    def longestPalindrome(self,s):
        n=len(s)
        ans_left=ans_right=0

        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right-ans_left:
                ans_left,ans_right=l+1,r

        for i in range(n):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right-ans_left:
                ans_left,ans_right=l+1,r
            return s[ans_left:ans_right]