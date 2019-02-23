class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_header = ListNode(None)
        result = ListNode(0)
        result_header.next = result
        while (l1 != None) or (l2 != None):
            if (l1 != None) and (l2 != None):
                result.val += (l1.val + l2.val)
                
                if result.val >= 10:
                    result.val -= 10
                    result.next = ListNode(1)
                else:
                    result.next = ListNode(0)
                
                result = result.next
                l1 = l1.next
                l2 = l2.next
            elif l1 == None:
                result.val += l2.val
                if result.val >= 10:
                    result.val -= 10
                    result.next = ListNode(1)
                else:
                    result.next = ListNode(0)
                
                result = result.next
                l2 = l2.next
            elif l2 == None:
                result.val += l1.val
                if result.val >= 10:
                    result.val -= 10
                    result.next = ListNode(1)
                else:
                    result.next = ListNode(0)
                
                result = result.next
                l1 = l1.next
        
        # removes the tailing zero
        temp = result_header
        while temp.next.next != None:
            temp = temp.next
        
        if temp.next.val == 0:
            temp.next = None

        
        return result_header.next

if __name__ == "__main__":
    solu = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = solu.addTwoNumbers(l1, l2)
    result_str = ''
    while result != None:
        result_str += str(result.val)
        result = result.next
    print(list(reversed(result_str)))
    
