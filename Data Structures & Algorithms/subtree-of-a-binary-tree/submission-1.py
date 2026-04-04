# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(node, sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            if node.val == sub.val and isSame(node.left, sub.left) and isSame(node.right, sub.right):
                return True
            
        def dfs(node):
            if not node:
                return False
            if isSame(node, subRoot):
                return True
            if dfs(node.right) or dfs(node.left):
                return True
            else:
                return False
        if not subRoot:
            return True
        return dfs(root)
        