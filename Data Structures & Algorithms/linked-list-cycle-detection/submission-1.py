# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers
        slow = head
        fast = head

        while fast and fast.next:
            # increment slow forward by 1 & fast by 2
            slow = slow.next
            fast = fast.next.next

            # if slow & fast meet, then cycle confirmed
            if slow == fast:
                return True

        # if fast exited while loop, can't have cycle
        return False