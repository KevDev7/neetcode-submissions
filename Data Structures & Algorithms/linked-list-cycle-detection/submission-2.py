# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # while next 2 nodes exist
        while fast and fast.next:
            # increment slow forward by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False

