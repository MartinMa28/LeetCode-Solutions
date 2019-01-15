# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode('header')
        cur = new_head
        while True:
            if l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = cur.next
                    l2 = l2.next
            elif l1 == None:
                cur.next = l2
                return new_head.next
            elif l2 == None:
                cur.next = l1
                return new_head.next

def create_linked_list(seq_list):
    new_head = ListNode('header')
    prev_node = new_head
    length = len(seq_list)
    for i in range(length):
        new_node = ListNode(seq_list[i])
        prev_node.next = new_node
        prev_node = new_node

    return new_head.next

if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [3, 5, 6]
    l_l1 = create_linked_list(l1)
    l_l2 = create_linked_list(l2)

    solu = Solution()
    new_head = solu.mergeTwoLists(l_l1, l_l2)
    print(new_head)

