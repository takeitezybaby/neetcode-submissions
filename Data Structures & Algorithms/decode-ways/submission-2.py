class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def decode(s,n) :
            dp = [0] * (n+1)
            dp[n] = 1
            for i in range(n-1,-1,-1) :
                if s[i] == '0' :
                    dp[i] = 0
                    continue
                one_digit = dp[i+1]
                two_digit = 0
                if i+1<n and 10<=int(s[i:i+2])<=26:
                    two_digit = dp[i+2]
                dp[i] = one_digit+two_digit
            return dp[0]
        return decode(s,n)
