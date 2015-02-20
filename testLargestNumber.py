'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

def compare(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a == size_b:
        return cmp(a, b)
    elif size_a < size_b:
        return cmp(a, b[:size_a]) or compare(a, b[size_a:])
    else:
        return cmp(a[:size_b], b) or compare(a[size_b:], b)


class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        result = ''.join(sorted(map(int.__str__, num), cmp = compare, reverse=True)).lstrip('0')
        return result or '0'
        

import unittest

class TestLargestNumber(unittest.TestCase):
    def testLargestNumber(self):
        sol = Solution()
        self.assertEqual('9534330', sol.largestNumber([3, 30, 34, 5, 9]))
        self.assertEqual('0', sol.largestNumber([0, 0, 0]))

if __name__ == '__main__':
    unittest.main()
