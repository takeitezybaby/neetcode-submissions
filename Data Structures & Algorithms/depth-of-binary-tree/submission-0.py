# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        
        def get_depth(n) :
            if n is None : 
                return 0
            dl = get_depth(n.left)
            dr = get_depth(n.right)
            return 1 + max(dl,dr)
        return get_depth(root)
            