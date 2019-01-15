# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
            return (None, 0)
        
        seq = []
        while head != None:
            seq.append(head.val)
            head = head.next

        return (create_reversed_linked_list(seq), len(seq))
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reversed_head, length = self.reverseList(head)

        for i in range(int(length / 2)):
            if head.val != reversed_head.val:
                return False
            
            head = head.next
            reversed_head = reversed_head.next
        
        return True

        
        
        