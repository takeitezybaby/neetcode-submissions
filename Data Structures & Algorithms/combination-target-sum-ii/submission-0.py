class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(candidates)
        def backtrack(start, remaining, path) :
            if remaining == 0 :
                result.append(path.copy())
            for i in range(start, len(nums)) :
                if nums[i] > remaining :
                    break
                if nums[i] == nums[i-1] and i>start :
                    continue
                path.append(nums[i])
                backtrack(i+1, remaining-nums[i], path)
                path.pop()
        backtrack(0,target,[])
        return result
