class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j] = is s[i..j] a palindrome

        best_start, best_length = 0, 1  # every single char is a palindrome of length 1

        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j] and length > best_length:
                    best_start, best_length = i, length

        return s[best_start : best_start + best_length]