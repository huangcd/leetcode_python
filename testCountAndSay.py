'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        idx = 1
        while idx < n:
            idx += 1
            tmp = ''
            last = None
            for c in s:
                if not last:
                    last = c
                    count = 1
                elif c == last:
                    count += 1
                else:
                    tmp = tmp + str(count) + last
                    last = c
                    count = 1
            tmp = tmp + str(count) + last
            s = tmp
        return s
                

import unittest

class Test_testCountAndSay(unittest.TestCase):
    def test_A(self):
        sol = Solution()
        self.assertEqual('1', sol.countAndSay(1))
        self.assertEqual('11', sol.countAndSay(2))
        self.assertEqual('21', sol.countAndSay(3))
        self.assertEqual('1211', sol.countAndSay(4))

if __name__ == '__main__':
    unittest.main()
