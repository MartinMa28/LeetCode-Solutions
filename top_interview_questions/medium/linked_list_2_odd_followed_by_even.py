import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        odds = copy.deepcopy(head)
        odds_header = odds
        while odds.next != None:
            if odds.next.next != None:
                odds.next = odds.next.next
                odds = odds.next
            else:
                break
        
        evens = copy.deepcopy(head.next)
        evens_header = evens
        while evens.next != None:
            evens.next = evens.next.next
            evens = evens.next
            if evens == None:
                break
        
        
        odds.next = evens_header
        return odds_header

if __name__ == "__main__":
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)
    ll.next.next.next.next.next = None
    solu = Solution()
    odd_even = solu.odd_even_list(ll)

    result_str = ''
    while odd_even != None:
        result_str += str(odd_even.val)
        odd_even = odd_even.next
    
    print(result_str)