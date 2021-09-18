'''
l1 = [1,2,4], l2 = [1,3,4]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwoLists(l1.next, l2)
    return l1 or l2
