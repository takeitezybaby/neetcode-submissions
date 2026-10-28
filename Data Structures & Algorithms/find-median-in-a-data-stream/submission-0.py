class MedianFinder:

    def __init__(self):
        self.ho = []
        self.lo = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.ho, -heapq.heappop(self.lo))
        if len(self.ho)>len(self.lo) :
            heapq.heappush(self.lo, -heapq.heappop(self.ho))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.ho) :
            return -self.lo[0]
        else :
            return (-self.lo[0]+self.ho[0])/2
        
        