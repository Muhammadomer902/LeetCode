# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1, root2):
        def is_flip_equivalent(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False

            return (is_flip_equivalent(node1.left, node2.left) and \
                    is_flip_equivalent(node1.right, node2.right)) or \
                   (is_flip_equivalent(node1.left, node2.right) and \
                    is_flip_equivalent(node1.right, node2.left))

        return is_flip_equivalent(root1, root2)
        