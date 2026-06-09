# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head

        return self.reverseListHelper(currentNode)

    def reverseListHelper(self, currentNode: Optional[ListNode]) -> Optional[ListNode]:
        if not currentNode or currentNode.next == None:
            return currentNode

        newHead = self.reverseListHelper(currentNode.next)
        
        nextNode = currentNode.next
        nextNode.next = currentNode
        currentNode.next = None

        return newHead