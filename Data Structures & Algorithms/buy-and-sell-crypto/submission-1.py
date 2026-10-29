class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, best = float("inf"), 0
        for p in prices :
            lo = min(p,lo)
            best = max(best,p-lo)
        return best