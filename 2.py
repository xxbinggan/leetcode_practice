# 作者:lixy
# 2026年08月16日17时54分14秒
# 2695016411@qq.com
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1,l2,carry=0):
        if l1 is None and l2 is None and carry==0:
            return None

        s=carry
        if l1:
            s+=l1.val
            l1=l1.next

        if l2:
            s+=l2.val
            l2=l2.next

        return ListNode(s%10,self.addTwoNumbers(l1,l2,s//10))
