# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            if len(arr) - 1 == k:
                return
            inorder(root.right)
        inorder(root)
        return arr[k-1]
