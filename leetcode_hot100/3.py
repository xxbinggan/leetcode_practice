# 作者:lixy
# 2026年08月16日20时20分52秒
# 2695016411@qq.com
class Solution:
    def lengthofLongestSubstring(self, s):
        occ=set()
        n=len(s)

        rk,ans=-1,0

        for i in range(n):
            if i!=0:
                occ.remove(s[i-1])
            while rk+1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk+=1
            ans=max(ans,rk-i+1)
        return ans
