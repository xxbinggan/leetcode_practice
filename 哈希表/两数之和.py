# 作者:lixy
# 2026年11月18日15时58分42秒
# 2695016411@qq.com
class Solution:
    def twoSum(self,nums,target):
        records=dict()

        for index,value in enumerate(nums):
            if target-value in records:
                return [records[target-value],index]
            records[value]=index
        return []