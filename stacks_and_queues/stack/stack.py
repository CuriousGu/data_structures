class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    # insert new item
    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size += 1

    # return item
    def pop(self):
        node = self.top
        self.top = self.top.next  # set new top with the right below
        if self._size > 0:
            self._size -= 1
            return node.data
        else:
            raise IndexError("Stack has 0 items")

    # return item, without popping it
    def peek(self):
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("Stack has 0 itemns")

    def __len__(self):
        return self._size

    def __repr__(self):
        txt, counter = "", 0
        pointer = self.top

        while counter < self._size:
            txt += f" {pointer.data} "
            pointer = pointer.next
            counter += 1

        return txt

    def __eq__(self, other_stack):
        if self._size != other_stack._size:
            return False

        counter = 0
        pointer_a, pointer_b = self.top, other_stack.top

        while counter < self._size and pointer_b.data == pointer_a.data:
            counter += 1
            pointer_a, pointer_b = pointer_a.next, pointer_b.next

        return counter == self._size
