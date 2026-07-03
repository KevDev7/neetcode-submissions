# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            # shift slow by 1
            slow = slow.next

            # shift fast by 2
            fast = fast.next.next

            # if fast & slow meet, then cycle confirmed
            if slow == fast:
                return True

        return False
        