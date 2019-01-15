# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        cur_node = head
        temp_node = head

        while True:
            if i < n:
                i += 1
                if cur_node.next == None:
                    head = head.next
                    return head
                cur_node = cur_node.next
            else:
                if (cur_node != None) and (cur_node.next != None):
                    cur_node = cur_node.next
                    temp_node = temp_node.next
                else:
                    if temp_node.next == None:
                        head = None
                    else:
                        temp_node.next = temp_node.next.next
                    break

        return head


h = ListNode(1)
h.next = ListNode(2)
# h.next.next = ListNode(3)
# h.next.next.next = ListNode(4)
# h.next.next.next.next = ListNode(5)

if __name__ == "__main__":
    solu = Solution()
    new_head = solu.removeNthFromEnd(h, 2)
    print(new_head)