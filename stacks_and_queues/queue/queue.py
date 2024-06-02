class Queue:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.root = None
        self._size = 0

    def append(self, item: int) -> None:
        if not self.root:
            self.root = Queue.Node(item)
        else:
            pointer = self.root
            while pointer.next:
                pointer = pointer.next
            pointer.next = Queue.Node(item)
        self._size += 1

    def remove(self) -> int:
        if not self.root:
            raise ValueError("Empty Queue")

        temp = self.root.value
        self.root = self.root.next
        self._size -= 1

        return temp

    def __str__(self):
        if not self.root:
            return '[]'

        pointer = self.root
        txt = f'{pointer.value} '
        while pointer.next:
            pointer = pointer.next
            txt += f'{pointer.value} '
        return txt

    def __len__(self):
        return self._size
