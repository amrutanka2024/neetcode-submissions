# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  # if both are None , than enen if 1 is None,than if boths values are None
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        L = self.isSameTree(p.left,q.left)
        R = self.isSameTree(p.right,q.right)

        return L and R
        
