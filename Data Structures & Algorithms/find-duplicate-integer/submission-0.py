class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = {}
        for num in nums :
            counts[num] = 1 + counts.get(num, 0)
            if counts[num] > 1:
                return num
        return None