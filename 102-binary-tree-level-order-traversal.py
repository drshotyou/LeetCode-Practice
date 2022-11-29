# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

#v2 better than 97% not sure about this
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        tree = traverse(root,tree,0)
        return tree
def traverse(root,tree,level):
    if(root):
        if( not (level< len(tree)-1)  ):
            tree.append([])
        tree[level].append(root.val)
        level+=1
        if(root.left):
            tree = traverse(root.left,tree,level)
        if(root.right):
            tree = traverse(root.right,tree,level)
        if( tree[len(tree)-1] == [] ):
            tree.pop()

    return tree
    
#v3 using "queue"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue:
            level = []
            l = len(queue)
            for i in range(l):
                curr = queue.pop(0)
                level.append(curr.val)
                if(curr.left):
                    queue.append(curr.left)
                if(curr.right):
                    queue.append(curr.right)
            ans.append(level)

        return ans

