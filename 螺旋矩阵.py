# 作者:lixy
# 2026年10月05日22时40分23秒
# 2695016411@qq.com
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums=[[0]*n for _ in range(n)]
        loop,mid=n//2,n//2
        startx,starty=0,0
        count=1

        for offset in range(1,loop+1):
            for i in range(starty,n-offset):
                nums[startx][i]=count
                count+=1
            for i in range(startx,n-offset):
                nums[i][n-offset]=count
                count+=1
            for i in range(n-offset,starty,-1):
                nums[n-offset][i]=count
                count+=1
            for i in range(n-offset,startx,-1):
                nums[i][startx]=count
                count+=1

            startx+=1
            starty+=1

        if n%2!=0:
            nums[mid][mid]=count

        return nums
