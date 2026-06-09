# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1Node, list2Node) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1Node and list2Node:
            if list1Node.val <= list2Node.val:
                tail.next = list1Node
                list1Node = list1Node.next
            else:
                tail.next = list2Node
                list2Node = list2Node.next
            
            tail = tail.next
        
        tail.next = list1Node if list1Node else list2Node
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        merged = lists[0]

        for i in range(1, len(lists)):
            merged = self.mergeTwoLists(merged, lists[i])

        return merged
        