# 作者:lixy
# 2026年10月22日17时38分44秒
# 2695016411@qq.com
# Definition for singly-linked list.
from typing import Optional
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)

        current=dummy_head
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next

        return dummy_head.next