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

    def __lte__(self, other):
        print(f'lenselfheap: {len(self.heap) and lenotherheap: {len(other.heap)}}')
        return len(self.heap) <= len(other.heap)

    def __str__(self):
        return f"MinHeap {[x for x in self.heap]}"
