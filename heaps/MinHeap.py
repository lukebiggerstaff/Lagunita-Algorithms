import heapq

class MinHeap(object):


    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        return heapq.heappop(self.heap)

    def getmin(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __lt__(self, other):
        return len(self.heap) < len(other.heap)

    def __str__(self):
        return "MinHeap {}".format([x for x in self.heap])
