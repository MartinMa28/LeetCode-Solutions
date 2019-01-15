class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        prev_node = None
        for i in nums:
            new_node = TreeNode(i)
            new_node.left = prev_node
            prev_node = new_node
        
        cur_node = new_node
        while cur_node.left != None:
            (cur_node.left).right = cur_node
            cur_node = cur_node.left
        
        center = int(len(nums) / 2)
        i = 0
        while i < center:
            cur_node = cur_node.right
            i += 1
        
        return cur_node

if __name__ == "__main__":
    solu = Solution()
    root = solu.sortedArrayToBST([-10,-3,0,5,9])
    print([root.left.left.val, root.left.val, root.val, root.right.val, root.right.right.val])