# coding=utf-8
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

represents = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        result = list(self.search(digits))
        return result
    
    def search(self, digits):
        if not digits:
            yield ''
        else:
            for c in represents[digits[0]]:
                for tail in self.search(digits[1:]):
                    yield c + tail

import unittest

class TestLetterCombinations(unittest.TestCase):
    def testLetterCombinations(self):
        sol = Solution()
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], sol.letterCombinations('23'))

if __name__ == '__main__':
    unittest.main()
