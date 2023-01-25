# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # print(root)
        return self.inverse(root)

    # og method not so fast   
    def traverse(self,root):
        if root:
            if root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
                self.traverse(root.left)
                self.traverse(root.right)
            elif root.left and root.right == None:
                temp = root.left
                root.left = None
                root.right = temp
                self.traverse(root.right)
            elif root.right and root.left == None:
                temp = root.right
                root.right = None
                root.left = temp
                self.traverse(root.left)

    # optimized method
    def inverse(self,root):
        if root:
            root.left,root.right = root.right,root.left
            root.left = self.inverse(root.left)
            root.right = self.inverse(root.right)
            return root
        else:
            return None

# Time complexity O(n) at most you have to visit all nodes to swap them
#  Space complexity O(1) we are not using any extra memory