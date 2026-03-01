# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goThroughAll(self, rpath, path, root):
        if not root:
            return
        
        if not root.right and not root.left:
            path += str(root.val) 
            rpath.append(path)
        else:
            path += str(root.val) + "->"
        self.goThroughAll(rpath, path, root.left)
        self.goThroughAll(rpath, path, root.right)


    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        rpath = [];path = ""

        self.goThroughAll(rpath, path,root)

        return rpath
