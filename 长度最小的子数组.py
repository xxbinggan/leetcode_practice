# 作者:lixy
# 2026年10月05日10时27分54秒
# 2695016411@qq.com
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        left=0
        right=0
        sum=0
        min_len=float('inf')
        while right<l:
            sum+=nums[right]

            while sum>=target:
                min_len=min(min_len, right-left+1)
                sum-=nums[left]
                left+=1

            right+=1

        return min_len if min_len!=float('inf') else 0