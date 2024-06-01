class BinaryTree:

    class Node:
        def __init__(self, value=None):
            self._left = None
            self._right = None
            self.value = value

    def __init__(self, root_value: int = None):
        '''
        root_value = tree's root. If NULL, tree will be created empty
        '''
        self.root = BinaryTree.Node(root_value)
        self.__size = 0 if not self.root else 1

    def __len__(self) -> int:
        return self.__size

    def __find_item_node(self, item: int) -> Node:
        pointer = self.root

        while pointer:
            if item == pointer.value:
                return pointer
            elif pointer.value >= item:
                pointer = pointer._left
            else:
                pointer = pointer._right

        return None

    def append(self, item: int) -> None:
        pointer = self.root

        while pointer:
            if pointer.value >= item:
                pointer = pointer._left
            else:
                pointer = pointer._right

        self.__size += 1
        pointer = BinaryTree.Node(item)
