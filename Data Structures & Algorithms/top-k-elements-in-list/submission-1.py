class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for num in nums :
            freq[num] = 1 + freq.get(num, 0)
                        
        sorted_num = []
        for num, f in freq.items() :
            sorted_num.append([f,num])
        sorted_num.sort()

        output = []
        while len(output) < k :
            output.append(sorted_num.pop()[1])

        return output
            