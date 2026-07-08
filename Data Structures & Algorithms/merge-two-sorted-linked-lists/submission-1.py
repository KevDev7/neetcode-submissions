# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create new linked list
        dummy = ListNode() # dummy will be head node of new list
        tail = dummy       # tail will point to end of new list
        
        # while list1 and list2 are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        # attach remainder of list1 or list2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

            
                