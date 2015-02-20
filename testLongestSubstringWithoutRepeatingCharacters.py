'''
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        indices = {}
        start = -1
        max_size = 0
        for idx, c in enumerate(s):
            if c in indices and indices[c] > start:
                start = max(start, indices[c])
            else:
                max_size = max(max_size, idx - start)
            indices[c] = idx
        return max_size
        

import unittest

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def testLengthOfLongestSubstring(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, sol.lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(12, sol.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'))

if __name__ == '__main__':
    unittest.main()
