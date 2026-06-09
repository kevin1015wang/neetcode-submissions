class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        lastNode = self.tail.prev

        lastNode.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = lastNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        firstNode = self.head.next

        newNode.next = firstNode
        firstNode.prev = newNode
        newNode.prev = self.head
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        value = self.tail.prev.val
        lastNode = self.tail.prev

        self.tail.prev = lastNode.prev
        self.tail.prev.next = self.tail
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next.val
        firstNode = self.head.next

        self.head.next = firstNode.next
        self.head.next.prev = self.head
        return value
        
