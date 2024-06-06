class DoublyLinkedList:

    class Node:
        def __init__(self, item: any) -> None:
            self.next = None
            self.previous = None
            self.value = item

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size
    
    def insert(self, index: int, item: any) -> None:
        '''
        index = A number specifying in which position to insert the value
        item =  An element of any type (string, number, object etc.)
        '''
        if index >= self._size:
            raise IndexError("list index out of range")
        else:
            pointer = self.head
            while index > 0:
                pointer = pointer.next
                index -= 1
            item = DoublyLinkedList.Node(item)
            item.next, item.previous = pointer, pointer.previous
            pointer.previous = item
            self.head = item

    def append(self, item: any) -> None:
        '''
        item =  An element of any type (string, number, object etc.)
        '''
        if not self.head:
            self.head = self.tail = DoublyLinkedList.Node(item)
            self._size += 1
        else:
            self.tail.next = DoublyLinkedList.Node(item)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

# pop, remove, index