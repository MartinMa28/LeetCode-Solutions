# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# def create_linked_circle_list(seq_list, pos):
#     head = ListNode('header')
#     cur = head
#     for i in range(len(seq_list)):
#         cur.next = ListNode(seq_list[i])
#         cur = cur.next
#     head = head.next
#     circled_node = head
#     for i in range(pos):
#         circled_node = head.next.next
#     cur.next = 

class Solution(object):
    def deprecated_has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes_list = []
        while head != None:
            if head in nodes_list:
                return True
            
            nodes_list.append(head) 
            head = head.next
        
        return False
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while True:
            if slow == None:
                return False
            elif fast == None:
                return False
            elif fast.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
            
            if slow == fast:
                return True