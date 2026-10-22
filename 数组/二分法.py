# 作者:lixy
# 2026年10月03日17时22分52秒
# 2695016411@qq.com
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if(nums[mid]<target):
                left=mid+1
            elif(nums[mid]>target):
                right=mid-1
            else:
                return mid
        return -1

