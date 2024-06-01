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
        pointer = self.root

        while pointer:
            if pointer.value >= item:
                pointer = pointer._left
            else:
                pointer = pointer._right

        self.__size += 1

        if item > pointer.value:
            pointer.right = BinaryTree.Node(item)
        else:
            pointer.left = BinaryTree.Node(item)

a = BinaryTree()
a.append(2)
print(len(a))