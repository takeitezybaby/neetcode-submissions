# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        def height_balance(n):
            if n is None :
                return (-1,True)
            left_balance = height_balance(n.left)
            right_balance = height_balance(n.right)

            hl, left_bal = left_balance
            hr, right_bal = right_balance
            if left_bal == False or right_bal == False :
                result  = False
            else : 
                if abs(hl-hr)<=1 : 
                    result = True
                else : 
                    result = False

            return (1+max(hl,hr), result)
        return height_balance(root)[-1]

