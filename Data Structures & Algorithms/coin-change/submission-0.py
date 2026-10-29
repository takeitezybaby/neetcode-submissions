from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize = None)
        def f(a) :
            if a==0 :
                return 0
            best = float("inf")
            for c in coins :
                if c<=a :
                    best = min(best,1+f(a-c))
            return best
        ans=f(amount)
        return ans if ans != float("inf") else -1
