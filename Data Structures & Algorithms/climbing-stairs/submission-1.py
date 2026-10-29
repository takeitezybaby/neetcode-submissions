class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1 :
            return 1
        step1 = 1
        step2 = 1
        for i in range(2,n+1) :
            temp = step2
            step2 = step1 + step2
            step1 = temp
        return step2