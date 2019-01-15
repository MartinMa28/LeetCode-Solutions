# Definition of a binary tree node
class node():
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def left_most_node(cur_node):
            if cur_node.left != None:
                return left_most_node(cur_node.left)
            else:
                return cur_node
        
        def right_most_node(cur_node):
            if cur_node.right != None:
                return right_most_node(cur_node.right)
            else:
                return cur_node

        def test_if_valid(cur_node):
            if cur_node == None:
                return True
            elif cur_node.left != None and cur_node.right != None:
                return (right_most_node(cur_node.left).val < cur_node.val) and \
                (cur_node.val < left_most_node(cur_node.right).val) and \
                test_if_valid(cur_node.left) and test_if_valid(cur_node.right)
            elif cur_node.left == None and cur_node.right != None:
                return (cur_node.val < left_most_node(cur_node.right).val) and test_if_valid(cur_node.right)
            elif cur_node.left != None and cur_node.right == None:
                return (right_most_node(cur_node.left).val < cur_node.val) and test_if_valid(cur_node.left)
            else:
                return True
        
        return test_if_valid(root)

if __name__ == "__main__":
    root = node(5)
    root.left = node(1)
    root.right = node(4)
    root.right.left = node(3)
    root.right.right = node(6)
    solu = Solution()
    print(solu.isValidBST(root))