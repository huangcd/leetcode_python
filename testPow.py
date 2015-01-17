'''
Implement pow(x, n)
'''

class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / pow(self, x, -n)
        cache = {1 : x}
        return self.calc(x, n, cache)
        
    def __pow__(self, x, n):
        return self.pow(x, n)

    def calc(self, x, n, cache):
        if n in cache:
            return cache[n]
        if n % 2 == 0:
            sqrt = self.calc(x, n / 2, cache)
            cache[n] = sqrt * sqrt
            return cache[n]
        else:
            less = self.calc(x, n / 2, cache)
            more = self.calc(x, n - n / 2, cache)
            cache[n] = less * more
            return cache[n]


import unittest

class TestPow(unittest.TestCase):
    def testPow(self):
        sol = Solution()
        self.assertEqual(sol.pow(120.0, 8), pow(120.0, 8))
        self.assertEqual(sol.pow(120.0, 7), pow(120.0, 7))
        self.assertEqual(sol.pow(120.0, 9), pow(120.0, 9))
        self.assertEqual(sol.pow(120.0, 0), pow(120.0, 0))
        self.assertEqual(sol.pow(120.0, 1), pow(120.0, 1))
        self.assertEqual(sol.__pow__(120, 9), pow(120, 9))

if __name__ == '__main__':
    unittest.main()