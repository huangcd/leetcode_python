'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def num2List(n):
    if n <= 0:
        return None
    header = ListNode(-1)
    p = header
    while n:
        p.next = ListNode(n % 10)
        n /= 10
        p = p.next
    return header.next

def list2Num(l):
    val = 0
    prod = 1
    while l:
        val = val + prod * l.val
        prod *= 10
        l = l.next
    return val

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        header = ListNode(-1)
        p = header
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + carry
                carry = val / 10
                p.next = ListNode(val % 10)
                p = p.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                carry = val / 10
                p.next = ListNode(val % 10)
                p = p.next
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                carry = val / 10
                p.next = ListNode(val % 10)
                p = p.next
                l2 = l2.next
        if carry:
            p.next = ListNode(carry)
            p = p.next
        return header.next

import unittest
class TestAddTwoNumber(unittest.TestCase):
    def testList2Num(self):
        self.assertEqual(243, list2Num(num2List(243)))
        l = num2List(243)
        self.assertEqual(3, l.val)
        l = l.next
        self.assertEqual(4, l.val)
        l = l.next
        self.assertEqual(2, l.val)

    def testAddTwoNumber(self):
        sol = Solution()
        self.assertEqual(343, list2Num(sol.addTwoNumbers(num2List(342), num2List(1))))
        self.assertEqual(807, list2Num(sol.addTwoNumbers(num2List(342), num2List(465))))

if __name__ == '__main__':
    unittest.main()
