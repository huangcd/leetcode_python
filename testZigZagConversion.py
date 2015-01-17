'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
'''

def alterJoin(a, b):
    return ''.join(map(lambda x, y: (x or '') + (y or ''), a, b))

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        length = 2 * nRows - 2
        array = [s[x::length] for x in xrange(length)]
        for i in xrange(1, length / 2):
            array[i] = alterJoin(array[i], array[length - i])
        return ''.join(array[:nRows])

import unittest

class TestZigZagConversion(unittest.TestCase):
    def testZigZag(self):
        sol = Solution()
        self.assertEqual("PAHNAPLSIIGYIR", sol.convert("PAYPALISHIRING", 3))
        self.assertEqual("ACBD", sol.convert("ABCD", 2))
        self.assertEqual("A", sol.convert("A", 1))

if __name__ == '__main__':
    unittest.main()
