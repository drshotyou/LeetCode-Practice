class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l,r):
            if l > r:
                return None

            m = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            return root
        return helper(0,len(nums)-1)

        # time complexity O(n)
        # space complexity O(n)