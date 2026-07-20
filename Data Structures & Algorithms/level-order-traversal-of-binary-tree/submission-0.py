# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        def dfs(node,level):
            if not node:
                return 
            # if same level repeats, but the res len is increased now my one so no match
            if level == len(res): 
                res.append([]) 

            res[level].append(node.val) # add in respective level 

            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0) # first execute this one where the node is given as root
        return res





