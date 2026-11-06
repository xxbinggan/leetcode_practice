# 作者:lixy
# 2026年11月06日15时56分50秒
# 2695016411@qq.com
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head=ListNode(0, head)

        slow=fast=dummy_head

        for i in range(n+1):
            fast=fast.next

        while fast:
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next

        return dummy_head.next