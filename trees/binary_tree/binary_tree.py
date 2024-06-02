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
        self.root = BinaryTree.Node(root_value) if root_value else None
        self.__size = 0 if not self.root else 1

    def __len__(self) -> int:
        return self.__size

    def append(self, item: int) -> None:
        if not self.root:
            self.root = BinaryTree.Node(item)
            self.__size += 1
            return

        pointer = self.root

        while pointer:
            if pointer.value > item and pointer._left:
                pointer = pointer._left
            elif pointer.value < item and pointer._right:
                pointer = pointer._right
            else:
                break

        if pointer.value < item:
            pointer._right = BinaryTree.Node(item)
        else:
            pointer._left = BinaryTree.Node(item)
        self.__size += 1

    def remove(self, item: int) -> None:
        pointer = self.root

        # finding node
        if not pointer.value:
            raise ValueError("Empty Tree")
        elif pointer.value == item:
            pass
        else:
            while pointer:
                if pointer.value < item:
                    parent = pointer
                    pointer = pointer._right
                elif pointer.value > item:
                    parent = pointer
                    pointer = pointer._left
                else:
                    break

        if pointer._right:
            replace_value = pointer._right
            while replace_value._left:
                parent = replace_value
                replace_value = replace_value._left
            pointer.value = replace_value.value
            parent._left = None
        elif pointer._left:
            replace_value = pointer._left
            while replace_value._right:
                parent = replace_value
                replace_value = replace_value._right
            pointer.value = replace_value.value
            parent._right = None
        else:
            if parent._left.value == item:
                parent._left = None
            else:
                parent._right = None
        self.__size -= 1
