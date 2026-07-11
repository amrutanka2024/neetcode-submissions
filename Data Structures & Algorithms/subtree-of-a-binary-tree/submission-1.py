# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

 # check after the two val. matches than check the left and right to make sure and return
        def sameRoot(R1 , R2):
            if not R1 and not R2:
                return True
            if  R1 and R2 and R1.val == R2.val:
                return (sameRoot(R1.left,R2.left) and sameRoot(R1.right,R2.right)) 
            return False
 # check weather the left and right subtree of both tree is identical 
        if not root:
            return False 
        if root.val == subRoot.val: # check weather the root value match if True than it might be the one
            if sameRoot(root,subRoot):
                return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))


        
