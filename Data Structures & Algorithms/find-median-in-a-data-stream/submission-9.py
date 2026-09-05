class MedianFinder:

    def __init__(self):
        self.firstHeap, self.secondHeap = [], [] # maxheap,  minheap

    def addNum(self, num: int) -> None:
        if self.secondHeap and num > self.secondHeap[0]:
            heapq.heappush(self.secondHeap, num)
        else:
            heapq.heappush(self.firstHeap, -num)
        if len(self.secondHeap) > (len(self.firstHeap) + 1):
           heapq.heappush(self.firstHeap, -heapq.heappop(self.secondHeap))
        if len(self.firstHeap) > (len(self.secondHeap) + 1):
            heapq.heappush(self.secondHeap, -heapq.heappop(self.firstHeap))

    def findMedian(self) -> float:
        if len(self.firstHeap) > len(self.secondHeap):
            return -self.firstHeap[0]
        elif len(self.secondHeap) > len(self.firstHeap):
            return self.secondHeap[0]
        return (self.secondHeap[0] + (-self.firstHeap[0])) / 2.0