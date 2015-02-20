# coding=utf-8
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while n:
            p = p.next
            n -= 1
        q = dummy
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummy.next

import unittest

class TestLetterCombinations(unittest.TestCase):
    def testLetterCombinations(self):
        sol = Solution()
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], sol.letterCombinations('23'))

if __name__ == '__main__':
    unittest.main()
