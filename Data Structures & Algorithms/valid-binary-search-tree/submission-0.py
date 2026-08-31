# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inbounds(node,low, high) :
            if not node :
                return True
            v = node.val
            return (v<high and v>low) and inbounds(node.left,low,v) and inbounds(node.right,v,high)

        return inbounds(root, float("-inf"), float("inf"))
