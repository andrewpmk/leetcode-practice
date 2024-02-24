# https://leetcode.com/problems/add-two-numbers/
# Time to solve: 30min

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def linked_list_to_string(self, l: ListNode) -> str:
        output = ""
        while l.next is not None:
            output += str(l.val)
            l = l.next
        output += str(l.val)
        return output

    def reverse_string(self, s: str) -> str:
        output = ""
        for i in range(len(s)-1,-1,-1):
            output += s[i]
        return output

    def reversed_string_to_linked_list(self, s: str) -> ListNode:
        n = None
        for i in range(len(s)):
            p = n
            n = ListNode(int(s[i]), p)
        return n

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Build strings
        string1 = self.linked_list_to_string(l1)
        string2 = self.linked_list_to_string(l2)
        # Reverse strings
        string1 = self.reverse_string(string1)
        string2 = self.reverse_string(string2)
        # Convert to integer
        int1 = int(string1)
        int2 = int(string2)
        # Add the numbers
        add = int1 + int2
        # Convert to string and build linked list
        return self.reversed_string_to_linked_list(str(add))


if __name__ == "__main__":
    solution = Solution()
    l1 = solution.reversed_string_to_linked_list("342")
    l2 = solution.reversed_string_to_linked_list("465")
    add = solution.addTwoNumbers(l1, l2)
    print(solution.reverse_string(solution.linked_list_to_string(add)))
    l1 = solution.reversed_string_to_linked_list("9999999")
    l2 = solution.reversed_string_to_linked_list("9999")
    add = solution.addTwoNumbers(l1, l2)
    print(solution.reverse_string(solution.linked_list_to_string(add)))