import heapq

class MaxHeap(object):


    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, (x * - 1))

    def pop(self):
        return (heapq.heappop(self.heap) * -1)

    def getmax(self):
        return self.heap[0] * -1

    def __len__(self):
        return len(self.heap)

    def __lt__(self, other):
        return len(self.heap) < len(other.heap)

    def __str__(self):
        return "MaxHeap {}".format([x for x in self.heap])
