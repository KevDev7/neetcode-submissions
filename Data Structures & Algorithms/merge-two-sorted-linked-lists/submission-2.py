# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make new linked list
        dummy = ListNode()  # dummy node to create 1st list node
        tail = dummy        # tail represents end of linked list

        while list1 and list2:
            # next node to linked based on which val is lower
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # move tail up
            tail = tail.next

        # fill in remainder of list1 or list2
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        # dummy.next is real head of new list
        return dummy.next

            
        

