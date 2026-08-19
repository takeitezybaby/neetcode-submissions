class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        while n>=1 :
            while stack and temperatures[stack[-1]] <= temperatures[n-1] :
                stack.pop()
            if stack :
                result[n-1] = stack[-1] - (n-1)
            else : 
                result[n-1] = 0
            stack.append(n-1)
            n-=1
        return result