# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(seq_list):
    header = ListNode('header')            # adds an explicit header node by convention
    prev = header
    cur = None
    for i in range(len(seq_list)):
        cur = ListNode(seq_list[i])
        prev.next = cur
        prev = cur

    return header.next                     # strips the header off node when returning

def create_reversed_linked_list(forward_seq_list):
    header = ListNode('header')
    prev = header
    cur = None
    length = len(forward_seq_list)
    for i in range(length):
        cur = ListNode(forward_seq_list[length - 1 - i])
        prev.next = cur
        prev = cur
    
    return header.next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        seq = []
        while head != None:
            seq.append(head.val)
            head = head.next

        return create_reversed_linked_list(seq)

if __name__ == "__main__":
    l = list(range(6))
    l_l = create_linked_list(l)
    solu = Solution()
    r_l = solu.reverseList(l_l)
    print(r_l)