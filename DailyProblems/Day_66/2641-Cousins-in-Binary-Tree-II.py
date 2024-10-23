# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root):
        def dfs_sum_values(node, depth):
            if node is None:
                return
            if len(depth_sums) <= depth:
                depth_sums.append(0)
            depth_sums[depth] += node.val
            dfs_sum_values(node.left, depth + 1)
            dfs_sum_values(node.right, depth + 1)

        def dfs_replace_values(node, depth):
            if node is None:
                return
            children_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            if node.left:
                node.left.val = depth_sums[depth] - children_sum
            if node.right:
                node.right.val = depth_sums[depth] - children_sum
            dfs_replace_values(node.left, depth + 1)
            dfs_replace_values(node.right, depth + 1)
        depth_sums = []
        dfs_sum_values(root, 0)
        root.val = 0
        dfs_replace_values(root, 1)
      
        return root