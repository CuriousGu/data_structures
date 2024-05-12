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
        pointer = self.top
        txt = ''
        while pointer:
            txt += f"/{pointer.data} "
            pointer = pointer.next

        txt += f"\nstack size = {self._size} items"
        return txt

    def __eq__(self, other_stack):
        pointer_a = self.top
        pointer_b = other_stack.top
        counter = 1

        while pointer_a.data == pointer_b.data and pointer_b.next and pointer_a.next:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
            counter += 1

        return True if counter == self._size and counter == other_stack._size else False
