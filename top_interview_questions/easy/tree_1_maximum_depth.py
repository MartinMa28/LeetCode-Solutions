# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Algorithm:
    # recursively find the height (maximum depth) of current node's sub-tree
    # in each iteration: If current node is not null, find the maximum depth of left and right depth,
    #                    return the max height of left and right sub-tree plus 1
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findHeight(cur_node):
            if cur_node == None:
                return 0
            else:
                left_height = findHeight(cur_node.left)
                right_height = findHeight(cur_node.right)
                return max(left_height, right_height) + 1
        
        height = findHeight(root)
        return height