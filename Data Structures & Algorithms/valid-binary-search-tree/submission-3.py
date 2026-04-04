# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            left_valid = dfs(node.left, min_val, node.val)
            right_valid = dfs(node.right, node.val, max_val)
            return left_valid and right_valid
        return dfs(root, float('-inf'), float('inf'))