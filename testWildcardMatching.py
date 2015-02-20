# coding=utf-8
'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ¡ú false
isMatch("aa","aa") ¡ú true
isMatch("aaa","aa") ¡ú false
isMatch("aa", "*") ¡ú true
isMatch("aa", "a*") ¡ú true
isMatch("ab", "?*") ¡ú true
isMatch("aab", "c*a*b") ¡ú false
'''
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        return self.__match__(s, p, {(0, 0): True, (1, 0): False})

    def __match__(self, s, p, cache):
        len_s = len(s)
        len_p = len(p)
        if (len_s, len_p) in cache:
            return cache[(len_s, len_p)]
        if not s and p[0] == '*':
            res = self.__match__(s, p[1:], cache)
            cache[(len_s, len_p)] = res
            return res
        if not p or not s:
            cache[(len_s, len_p)] = False
            return False
        head_s = s[0]
        head_p = p[0]
        if head_p == '?' or head_p == head_s:
            res = self.__match__(s[1:], p[1:], cache)
            cache[(len_s, len_p)] = res
            return res
        if head_p == '*':
            res = self.__match__(s[1:], p[1:], cache) or self.__match__(s[1:], p, cache)
            cache[(len_s, len_p)] = res
            return res
        return False

import unittest

class Test_testWildcardMatching(unittest.TestCase):
    def test_A(self):
        sol = Solution()
        self.assertFalse(sol.isMatch('aa','a'))
        self.assertTrue(sol.isMatch('aa', 'aa'))
        self.assertFalse(sol.isMatch('aa','aaa'))
        self.assertTrue(sol.isMatch('aa', '*'))
        self.assertTrue(sol.isMatch('aa', 'a*'))
        self.assertFalse(sol.isMatch('aab', 'c*a*b'))
        self.assertTrue(sol.isMatch('ab', '?*'))
        self.assertFalse(sol.isMatch('aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba', 'a*******b'))


if __name__ == '__main__':
    unittest.main()
