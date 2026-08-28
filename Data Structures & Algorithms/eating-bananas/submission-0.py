from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = float("inf")
        def cal_hours(list,k) :
            hours = 0
            for pile in list :
                hours += ceil(pile/k)
            return hours
        s_piles = sorted(piles, reverse = True)
        low = 1
        high = s_piles[0]
        while low <= high :
            mid = (low+high)//2
            if cal_hours(s_piles, mid) <= h :
                result = int(min(result, mid))
                high = mid-1
            else :
                low = mid + 1
        return result