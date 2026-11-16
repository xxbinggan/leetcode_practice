# 作者:lixy
# 2026年11月16日17时42分26秒
# 2695016411@qq.com
class Solution:
    def intersection(selfself,nums1,nums2):
        table={}
        for num in nums1:
            table[num]=table.get(num,0)+1
        res=set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]

        return list(res)