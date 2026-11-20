# 作者:lixy
# 2026年11月20日15时33分57秒
# 2695016411@qq.com
class Solution:
    def threeSum(self,nums):
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                return result

            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1

            while right>left:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_<0:
                    left+=1
                elif sum_>0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while left<right and nums[left]==nums[left+1]:
                        left+=1

                    right-=1
                    left+=1

        return result