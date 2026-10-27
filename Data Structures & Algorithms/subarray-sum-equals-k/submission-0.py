class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Fsums = {0:1}
        ans = 0
        s = 0
        for num in nums :
            s += num
            ans += Fsums.get(s-k,0)
            Fsums[s] = Fsums.get(s,0) + 1
        return ans