class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j] = is s[i..j] a palindrome
        count = 0

        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j] :
                    count+=1

        return count