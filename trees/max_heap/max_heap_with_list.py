class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item: int):
        self.heap.append(item)
        self.__reorder_insertion(len(self.heap) - 1)

    def remove_max(self) -> int:
        if len(self.heap) > 0:
            item = self.heap[0]
            self.__reorder_removal()
            return item
        else:
            return None

    def __reorder_insertion(self, item_index: int):
        while item_index > 0:
            parent_index = (item_index - 1) // 2
            if self.heap[parent_index] < self.heap[item_index]:
                self.heap[parent_index], self.heap[item_index] = self.heap[item_index], self.heap[parent_index]
                item_index = parent_index
            else:
                break

    def __reorder_removal(self):
        index = 0
        self.heap[index] = self.heap[-1]
        self.heap.pop()

        while 2 * index + 1 < len(self.heap):
            l_child = 2 * index + 1
            r_child = 2 * index + 2
            largest = index

            if l_child < len(self.heap) and self.heap[l_child] > self.heap[largest]:
                largest = l_child

            if r_child < len(self.heap) and self.heap[r_child] > self.heap[largest]:
                largest = r_child

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def __str__(self) -> str:
        leaves = 1
        txt = f"{str(self.heap[0:1])}\n"
        SIZE = len(self.heap)
        while 2**(leaves+1) - 1 < SIZE:
            txt += str(self.heap[2**leaves - 1: 2**(leaves+1) - 1]) + "\n"
            leaves += 1
        txt += str(self.heap[2**(leaves) - 1: SIZE])
        return txt
