# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. build a hashmap: value -> its index in inorder
        idx_map = {inorder[i]:i for i in range(len(inorder))}  # fill this in

        preidx = 0  # or use a list [0] / nonlocal, since it must persist

        def helper(inStart, inEnd):
            nonlocal preidx
            # 2. base case: what condition means "no nodes left to build"?
            if inStart>inEnd:
                return None

            # 3. get root value from preorder using the pointer
            root_val = preorder[preidx]
            # 4. advance the pointer (don't forget this)
            preidx+=1

            root = TreeNode(root_val)

            # 5. find root's position in inorder using idx_map
            i = idx_map[root.val]

            # 6. recurse LEFT first (why left first? — you already answered this)
            root.left = helper(inStart,i-1)
            # 7. then recurse RIGHT
            root.right = helper(i+1,inEnd)

            return root

        return helper(0, len(inorder) - 1)