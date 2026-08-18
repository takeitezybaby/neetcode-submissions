class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        stack = []

        # nearest smaller to the left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = i - (stack[-1] if stack else -1) - 1
            stack.append(i)

        stack = []
        # nearest smaller to the right
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = (stack[-1] if stack else n) - i - 1
            stack.append(i)

        return max(heights[i] * (left[i] + right[i] + 1) for i in range(n))