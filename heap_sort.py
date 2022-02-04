from distutils.command.build import build


class Heaptree():
    def __init__(self):
        self.heap = []
        self.size = 0
        self.sorted = []
    def data_down(self, i):
        while(i * 2 + 2 <= self.size):
            min_index = self.get_min_index(i)
            if self.heap[min_index] < self.heap[i]:
                self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            i = min_index
    def get_min_index(self, i):
        if i * 2 + 2 >= self.size:
            return i * 2 + 1
        else:
            if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
    def build_heap(self, mylist):
        i = (len(mylist) // 2) - 1
        self.heap = mylist
        self.size = len(mylist)
        while(i >= 0):
            self.data_down(i)
            i -= 1
    def sort_heap(self):
        while(self.heap):
            self.sorted.append(self.heap.pop(0))
            self.build_heap(self.heap)

test_list = [10, 21, 5, 9, 13, 28, 3, 8]
print('origin list:', test_list)
tree = Heaptree()
tree.build_heap(test_list)
print('heap tree:  ', tree.heap)
tree.sort_heap()
print('heap sorted:', tree.sorted)