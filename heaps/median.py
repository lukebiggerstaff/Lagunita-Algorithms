import sys

import MinHeap, MaxHeap

class TwoHeaps(object):

    def __init__(self):
        self.maxh = MaxHeap.MaxHeap()
        self.minh = MinHeap.MinHeap()
        self.medians = list()

    def add_to_heaps(self, value):
        if len(self.maxh.heap) == 0 and len(self.minh.heap) == 0:
            self.maxh.push(value)
            self.adjust_heaps()
        elif len(self.minh.heap) == 0:
            if value < self.maxh.getmax():
                self.maxh.push(value)
                self.adjust_heaps()
            else:
                self.minh.push(value)
                self.adjust_heaps()
        else:
            if value < self.maxh.getmax():
                self.maxh.push(value)
                self.adjust_heaps()
            else:
                self.minh.push(value)
                self.adjust_heaps()

    def adjust_heaps(self):
        if abs(len(self.minh) - len(self.maxh)) > 1:
            if len(self.minh) > len(self.maxh):
                self.maxh.push(self.minh.pop())
            else:
                self.minh.push(self.maxh.pop())

    def find_current_median(self):
        if len(self.minh) == len(self.maxh):
            self.medians.append( (self.minh.getmin() + self.maxh.getmax()) / 2 )
        elif len(self.minh) > len(self.maxh):
            self.medians.append( self.minh.getmin() )
        else:
            self.medians.append( self.maxh.getmax() )

def compute_medians(inputfile):
    heaps = TwoHeaps()
    with open(inputfile) as f:
        for line in f:
            heaps.add_to_heaps(line)
            heaps.find_current_median()
    total = 0;
    for each in heaps.medians:
        total += each
    print(f'{total % 10000}')


if __name__ == '__main__':
    compute_medians(sys.argv[1])
