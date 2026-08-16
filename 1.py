# 作者:lixy
# 2026年07月25日22时10分52秒
# 2695016411@qq.com
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


    def twosum2(self, nums, target):
        for i in range(len(nums)):
            res=target-nums[i]
            if res in nums[i+1:]:
                return [i,nums.index(res)]

if __name__ == '__main__':
    s=Solution()
    #print(s.twoSum([4,5,6,7],9))
    print(s.twosum2([2,3,5,7],7))