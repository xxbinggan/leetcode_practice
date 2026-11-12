# 作者:lixy
# 2026年11月12日17时05分12秒
# 2695016411@qq.com
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self,head):
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next

                return slow

        return None