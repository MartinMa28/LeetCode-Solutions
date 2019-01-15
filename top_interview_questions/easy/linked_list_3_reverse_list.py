# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(seq_list):
    new_head = ListNode('header')
    prev_node = new_head
    length = len(seq_list)
    for i in range(length):
        new_node = ListNode(seq_list[i])
        prev_node.next = new_node
        prev_node = new_node

    return new_head.next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        seq_list = []
        def recur(cur_node):
            seq_list.append(cur_node.val)
            if cur_node.next != None:
                recur(cur_node.next)
        
        recur(head)
        new_head = ListNode('header')      # add a special header in front of normal nodes
        prev_node = new_head
        length = len(seq_list)
        for i in range(length):
            new_node = ListNode(seq_list[length - 1 - i])
            prev_node.next = new_node
            prev_node = new_node

        return new_head.next           # strip off that special header

        
if __name__ == "__main__":
    seq = list(range(3))
    head = create_linked_list(seq)
    
    solu = Solution()
    new_head = solu.reverseList(head)
    print(new_head)