class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def mincost(n,cost) :
            
            prev1 = 0
            prev2 = 0
            for i in range(2, n+1) :
                temp = prev2
                prev2 = min(prev2+cost[i-1], prev1+cost[i-2])
                prev1 = temp
            return prev2
        n = len(cost)
        return mincost(n,cost)
        