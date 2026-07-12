class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)) :
            j = 0
            product = 1
            for j in range(len(nums)) :
                if j == i :
                    continue
                else :
                    product *= nums[j]
            result.append(product)
        return result
