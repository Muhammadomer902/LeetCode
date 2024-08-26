"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.out = [] 
    def postorder(self, root):
        if not root:
            return self.out
        for child in root.children:
            self.postorder(child)
        self.out.append(root.val)
        return self.out
        