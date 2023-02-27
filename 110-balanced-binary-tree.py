# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            def height(root):
                if not root: return True, 0
                leftBalanced, left = height(root.left)
                if not leftBalanced:
                    return False, 0
                rightBalanced, right = height(root.right)
                if not rightBalanced or abs(left - right) > 1:
                    return False, 0
                return True , max(left,right) + 1
            return height(root)[0]
        