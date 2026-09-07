class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(n, nums) :
            if n == 0 or n==1:
                return nums[0]
            prev1 = nums[0]
            prev2 = max(nums[0], nums[1])
            for i in range(2,n) :
                temp = prev2
                prev2 = max(nums[i] + prev1, prev2)
                prev1 = temp
            return prev2
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(backtrack(n-1,nums[0:n-1]), backtrack(n-1,nums[1:n]))