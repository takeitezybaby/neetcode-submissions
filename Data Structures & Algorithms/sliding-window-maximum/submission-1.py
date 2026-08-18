class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []  # Stores (-val, index)
        output = []

        for i, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, i))

      # Once the window reaches size k:
            if i >= k - 1:
        # Lazily remove top elements outside the current window
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)

                output.append(-max_heap[0][0])

        return output