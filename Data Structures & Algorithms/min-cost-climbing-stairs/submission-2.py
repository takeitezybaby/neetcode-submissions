class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def mincost(n,cost, result) :
            if n == 0 :
                result[n] = 0
                return result[n]
            if n == 1 :
                result[n] = 0
                return result[n]
            if n in result :
                return result[n]
            result[n] = min(mincost(n-1,cost,result)+cost[n-1], mincost(n-2,cost,result)+cost[n-2])
            return result[n]
        n = len(cost)
        return mincost(n,cost,{})
        