# 作者:lixy
# 2026年07月25日21时41分29秒
# 2695016411@qq.com
class Solution(object):
    def maxProduct(self, n):
        s=str(n)
        s=list(s)
        s=[int(x) for x in s]
        s.sort()
        return s[-1]*s[-2]

if __name__ == '__main__':
    s=Solution()
    print(s.maxProduct(789))
