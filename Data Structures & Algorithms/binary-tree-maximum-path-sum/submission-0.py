# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        best = float('-inf')

        def recurse(node):
            nonlocal best
            if not node:
                return 0

            left_chain = max(0, recurse(node.left))
            right_chain = max(0, recurse(node.right))

            # turning point sum (uses both sides) — candidate for the answer, not returned
            turning_point_sum = node.val + left_chain + right_chain
            best = max(best, turning_point_sum)

            # downward chain (uses at most one side) — this is what goes back to the parent
            return node.val + max(left_chain, right_chain)

        recurse(root)
        return best
        