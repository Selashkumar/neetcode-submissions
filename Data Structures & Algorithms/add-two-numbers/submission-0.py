# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        output = dummy
        first = l1
        second = l2
        a = b = count = 0
        while first:
            a += first.val * (10 ** count)
            count +=1
            first = first.next
        count = 0
        while second:
            b += second.val * (10 ** count)
            count +=1
            second = second.next
        ans = a + b
        while ans:
            output.val = ans % 10
            ans = ans // 10
            if ans:
                output.next = ListNode()
                output = output.next
        return dummy
