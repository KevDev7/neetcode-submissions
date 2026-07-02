# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy to be head node of new linked list
        dummy = ListNode()

        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                # create next node with smaller list1 value
                tail.next = list1
                list1 = list1.next
            else:
                # create next node with smaller list2 value
                tail.next = list2
                list2 = list2.next
            
            # move tail up 1
            tail = tail.next
        
        # while loop ends when either list1 or list2 empty, so other list can still have remaining nodes
        if list1:
            # add the remainder of list1
            tail.next = list1
        elif list2:
            # add the remainder of list2
            tail.next = list2
        
        # dummy is fake head, dummy.next is real head
        return dummy.next 
