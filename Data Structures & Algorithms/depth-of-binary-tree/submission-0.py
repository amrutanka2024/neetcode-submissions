# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = [[root,1]]
        depth = 0

        while stk:
            node , lvl = stk.pop()
            if node:
                stk.append([node.left , lvl + 1])
                stk.append([node.right , lvl + 1])
                depth = max(depth,lvl)
        return depth