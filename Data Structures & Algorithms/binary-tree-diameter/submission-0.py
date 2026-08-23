# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(n):
            if n is None:
                return -1
            hL = height(n.left)
            hR = height(n.right)
            self.max_diameter = max(self.max_diameter, hL + hR + 2)
            return 1 + max(hL, hR)

        height(root)
        return self.max_diameter
        