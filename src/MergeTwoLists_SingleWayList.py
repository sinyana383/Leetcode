from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        ptr = head

        while list1 is not None or list2 is not None:
            if list1 is None:
                ptr.next = list2
                break
            if list2 is None:
                ptr.next = list1
                break
            if list1.val <= list2.val:
                ptr.next = list1
                ptr = list1
                list1 = list1.next
            else:
                ptr.next = list2
                ptr = list2
                list2 = list2.next
        return head


# Helper function to create a linked list
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Test case
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 5])

solution = Solution()
merged = solution.mergeTwoLists(l1, l2)

print_linked_list(merged)