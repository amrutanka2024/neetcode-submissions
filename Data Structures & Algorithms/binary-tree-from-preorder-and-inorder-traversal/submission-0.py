# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None

        indx = inorder.index(preorder[0]) 

        L_inodr = inorder[:indx]
        R_inodr = inorder[indx+1:]

        L_preodr = preorder[1:indx+1]
        R_preodr = preorder[indx+1:]

        root = TreeNode(preorder[0]) # creating a node value of 
        root.left = self.buildTree( L_preodr, L_inodr )
        root.right = self.buildTree( R_preodr, R_inodr )
        return root


       
        