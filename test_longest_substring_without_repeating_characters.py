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

import nose

def test_solution():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcdef") == 6

if __name__ == '__main__':
    nose.runmodule()
