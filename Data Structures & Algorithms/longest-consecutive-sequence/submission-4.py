class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        sorted_list = sorted(set(nums))
        count = 1
        highest = 1
        for i in range(len(sorted_list)-1) :
            if sorted_list[i]+1 == sorted_list[i+1] :
                count += 1
            else : 
                if count>highest :
                    highest = count
                count = 1
        if count > highest:
            return count
        else :
            return highest
