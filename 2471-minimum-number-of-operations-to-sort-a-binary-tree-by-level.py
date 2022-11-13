class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = []
        level = 0
        def traverse(root,level):
            if(root):
                if(len(levels)<level):
                    levels.append([])
                    
                levels[level].append(root.val)
                level+=1
                levels = traverse(root.left,level)
                levels = traverse(root.right,level)
            
            return levels
            
                