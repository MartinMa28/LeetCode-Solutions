class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_mirror(self, left_root, right_root):
        if left_root != None and right_root != None:
            if left_root.val == right_root.val:
                return (self.is_mirror(left_root.left, right_root.right) \
                and \
                self.is_mirror(left_root.right, right_root.left))
            else:
                return False
        elif left_root == right_root:
            # both left and right roots are None
            return True
        else:
            # either one side is None, while the other side is not, so not mirror
            return False

    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.is_mirror(root.left, root.right)