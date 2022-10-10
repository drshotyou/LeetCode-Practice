# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current = root
        return traverse(current, float('-inf'), float('inf'))
        
        
def traverse(current,left, right):
    if not current:
        return True
    if not (current.val < right and current.val > left):
        return False
    return (traverse(current.left, left, current.val) and traverse(current.right, current.val, right))