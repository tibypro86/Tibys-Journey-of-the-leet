# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1
        def buildtree(start,end):
            if start > end:
                return
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = buildtree(start,mid-1)
            root.right = buildtree(mid+1,end)
            return root
        return buildtree(start,end)