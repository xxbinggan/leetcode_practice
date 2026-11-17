# 作者:lixy
# 2026年11月17日15时39分16秒
# 2695016411@qq.com
class Solution:
    def isHappy(self,n):
        record=set()

        while True:
            n=self.get_sum(n)
            if n==1:
                return True
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n):
        new_sum=0
        while n:
            n,r=divmod(n,10)
            new_sum+=r**2
        return new_sum