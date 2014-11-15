# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        else: 
            return self.findMinDepth(root)
    def findMinDepth(self, node):
        if node.left == None and node.right == None:
            return 1
        elif node.left == None and node.right != None:
            return 1 + self.findMinDepth(node.right)
        elif node.left != None and node.right == None:
            return 1 + self.findMinDepth(node.left) 
        else:
            return 1 + min(self.findMinDepth(node.left), self.findMinDepth(node.right))
        
