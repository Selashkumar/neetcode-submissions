# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            tempList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                tempList.append(self.mergeList(l1, l2))
            lists = tempList
        return lists[0]
    def mergeList(self, list1, list2):
        dummy = ListNode()
        mainList = dummy
        while list1 and list2:
            if list1.val > list2.val:
                mainList.next = list2
                list2 = list2.next
            else:
                mainList.next = list1
                list1 = list1.next
            mainList = mainList.next
        if list1:
            mainList.next = list1
        if list2:
            mainList.next = list2
        return dummy.next
