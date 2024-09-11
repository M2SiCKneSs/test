# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(root):
            if root is None:
                return 0
            else:
                left_depth = maxDepth(root.left)
                right_depth = maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        depth = maxDepth(root)
        return depth
        