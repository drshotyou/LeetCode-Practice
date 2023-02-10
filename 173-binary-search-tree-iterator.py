# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        current = root
        self.arr = []
        self.k = 0

        def inorder(root):
            if not root: 
                return
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        inorder(current)

    def next(self) -> int:
        ans = self.array[self.k]
        self.k += 1
        return ans
    def hasNext(self) -> bool:
        return self.k < len(self.arr)