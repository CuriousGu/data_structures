class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def append(self, item: any) -> None:
        self._size += 1
        if not self.head:
            self.head = Node(item)
            return
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = Node(item)

    def remove(self, index: int) -> None:
        if self._size > index:
            child_node = self.head
            parent_node = None
            for _ in range(index):
                parent_node = child_node
                child_node = child_node.next
            parent_node.next = child_node.next
            self._size -= 1
        else:
            raise IndexError()

    def index(self, item: any) -> int:
        pointer = self.head
        curr_index = 0
        while pointer:
            if pointer.data == item:
                return curr_index
            else:
                curr_index += 1
                pointer = pointer.next

    def __len__(self) -> int:
        return self._size

    def __setitem__(self, index: int, value: any) -> None:
        if self._size > index:
            pointer = self.head
            for _ in range(index):
                pointer = pointer.next
            pointer.data = value
        else:
            raise IndexError()

    def __getitem__(self, index: int) -> any:
        if self._size > index:
            pointer = self.head
            for _ in range(index):
                pointer = pointer.next
            return pointer.data
        else:
            raise IndexError()

    def __str__(self) -> str:
        pointer = self.head
        txt = ''
        for _ in range(self._size):
            txt += f"{pointer.data}, "
            pointer = pointer.next
        txt = txt[:-2]
        return txt