# 作者:lixy
# 2026年10月03日22时33分07秒
# 2695016411@qq.com
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast=0
        slow=0
        size=len(nums)
        while fast<size:
            if(nums[fast]!=val):
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            elif(nums[fast]==val):
                fast+=1
        return slow