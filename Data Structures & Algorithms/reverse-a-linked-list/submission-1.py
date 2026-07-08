# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # at start, there is no prev node, so it is None
        prev = None

        # curr starts at head of original linked list, & the node we're reversing
        curr = head

        # go until we reach end of original list, i.e. while curr is not None
        while curr:
            # Save temp before changing curr.next
            temp = curr.next

            # reverse pointer, curr points backward to prev
            curr.next = prev

            # move prev forward to the current node, now the front of the reversed part
            prev = curr

            # move curr forward to the next node from the original list
            curr = temp

        # When curr becomes None, prev points to the new head of the reversed linked list.
        return prev