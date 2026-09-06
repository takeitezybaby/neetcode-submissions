class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(path,start, nums) :
            nonlocal result
            result.append(path.copy())
            for i in range(start,len(nums)) :
                path.append(nums[i])
                backtrack(path,i+1,nums)
                path.pop()
        backtrack(path, 0, nums)
        return result