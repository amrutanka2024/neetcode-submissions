# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node , L , H):
            if not node:
                return True
            if not (L < node.val < H):
                return False
            return (dfs(node.left , L , node.val) and dfs(node.right , node.val , H))
# node fits range ? => left :(low , node) and right :(node , high) => both must valid 
        return dfs(root , float("-inf"),float("inf"))
