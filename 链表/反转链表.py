# 作者:lixy
# 2026年11月03日15时19分21秒
# 2695016411@qq.com
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        pre=None
        while cur:
            temp=cur.next
            cur.next=pre

            pre=cur
            cur=temp
        return pre