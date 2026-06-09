class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        newNode = ListNode(x)
        lastNode = self.tail.prev

        lastNode.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = lastNode

    def pop(self) -> int:
        lastNode = self.tail.prev
        newLastNode = lastNode.prev

        newLastNode.next = self.tail
        self.tail.prev = newLastNode

        return lastNode.val
        

    def top(self) -> int:
        lastNode = self.tail.prev
        return lastNode.val
        

    def empty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()