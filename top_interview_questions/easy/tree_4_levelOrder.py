# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        node_queue = list()
        level_queue = list()

        node_queue.insert(0, (root, 0))
        while len(node_queue) != 0:
            discovered = node_queue.pop(0)      # (node, current_depth)
            
            if len(level_queue) <= discovered[1]:
                level_queue.insert(discovered[1], [])
            level_queue[discovered[1]].append(discovered[0].val)

            
            if discovered[0].left != None:
                node_queue.append((discovered[0].left, discovered[1] + 1))
            if discovered[0].right != None:
                node_queue.append((discovered[0].right, discovered[1] + 1))
            
        return level_queue
                
                     