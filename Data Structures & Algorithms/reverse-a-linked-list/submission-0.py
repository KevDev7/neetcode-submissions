# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # [None (prev), 0 (curr), 1 (next_node), 2, 3, None]
        while curr is not None:
            # save temp
            next_node = curr.next

            # curr.next used to point forwards, make it point backwards (prev)
            curr.next = prev

            # move prev up 1 to curr
            prev = curr

            # move curr up 2 to next_node
            curr = next_node

        # while loop stops when curr points to None, thus prev points to new head
        return prev


            
