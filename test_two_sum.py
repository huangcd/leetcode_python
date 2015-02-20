'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
'''

class Solution:
    def twoSum(self, num, target):
        pairs = {}
        for idx, n in enumerate(num):
            if n in pairs:
                return (pairs[n] + 1, idx + 1)
            pairs[target - n] = idx
        return (-1, -1)

import unittest

class TestTwoSum(unittest.TestCase):
    def testTwoSum(self):
        sol = Solution()
        self.assertEqual((1, 2), sol.twoSum([2, 7, 11, 15], 9)) 
        self.assertEqual((1, 4), sol.twoSum([2, 11, 15, 7], 9)) 

if __name__ == '__main__':
    unittest.main()
