# https://leetcode.com/problems/merge-two-sorted-lists/
# Inefficient solution in 7 min 26 sec

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merge = []
        for l in (list1, list2):
            while l is not None:
                merge.append(l.val)
                l = l.next
        merge = sorted(merge)
        next = None
        node = None
        for i in range(len(merge)-1,-1,-1):
            node = ListNode(merge[i],next)
            next = node
        return node


if __name__ == "__main__":
    solution = Solution()

