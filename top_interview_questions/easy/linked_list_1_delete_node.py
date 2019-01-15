class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(4)
head.next = ListNode(5)
(head.next).next = ListNode(1)
head.next.next.next = ListNode(9)

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = head
        while cur != None:
            if cur.next.val == node:
                cur.next = cur.next.next
                break
            else: cur = cur.next

if __name__ == "__main__":
    solu = Solution()
    solu.deleteNode(5)
    print(head)