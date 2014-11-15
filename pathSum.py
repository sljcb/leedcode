# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # def hasPathSum(self, root, sum):
    #     return self.checkPath(root, sum)
    # def checkPath(self, node, sum):
    #     if node == None:
    #         return False
    #     if node.left == None and node.right == None:
    #         if sum == node.val:
    #             return True
    #         else: 
    #             return False
    #     else:
    #         return self.checkPath(node.left, sum-node.val) or self.checkPath(node.right, sum-node.val)
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            if sum == root.val:
                return True
            else: 
                return False
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
