# coding=utf-8
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ¡Ü b ¡Ü c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

def binary_search(arr, n, lo, hi):
    if lo >= hi:
        return -lo
    mid = (lo + hi) / 2
    if arr[mid] == n:
        return mid
    elif arr[mid] < n:
        return binary_search(arr, n, mid + 1, hi)
    return binary_search(arr, n, lo, mid)

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num = sorted(num)
        size = len(num)
        result = []
        for i in xrange(0, size):
            if i > 0 and num[i] == num[i - 1]:
                continue
            for j in xrange(i + 1, size):
                if j > i + 1 and num[j] == num[j - 1]:
                    continue
                search_val = - num[i] - num[j]
                k = binary_search(num, search_val, j + 1, size)
                if k > 0:
                    result.append([num[i], num[j], num[k]])
        return result

import unittest

class Test3Sum(unittest.TestCase):
    def test3Sum(self):
        sol = Solution()
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], sol.threeSum([-1, 0, 1, 2, -1, -4, -1, -1])) 

if __name__ == '__main__':
    unittest.main()
