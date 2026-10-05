# 作者:lixy
# 2026年10月05日09时53分02秒
# 2695016411@qq.com
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        k=len(nums)-1
        res=[float('inf')]*len(nums)
        while l<=r:
            if(nums[l]**2<nums[r]**2):
                res[k]=nums[r]**2
                r-=1
            else:
                res[k]=nums[l]**2
                l+=1
            k-=1
        return res
