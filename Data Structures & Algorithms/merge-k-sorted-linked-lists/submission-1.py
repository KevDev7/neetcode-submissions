# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add the head of each non-empty list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            # Get the node with the smallest value
            val, i, node = heapq.heappop(heap)

            # Attach that node to the merged list
            tail.next = node
            tail = tail.next

            # If this node has a next node, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next