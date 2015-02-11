'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        res = ''
        while num:
            if num >= 1000:
                num -= 1000
                res += 'M'
            elif num >= 900:
                num -= 900
                res += 'CM'
            elif num >= 500:
                num -= 500
                res += 'D'
            elif num >= 400:
                num -= 400
                res += 'CD'
            elif num > 100:
                num -= 100
                res += 'C'
            elif num > 90:
                num -= 90
                res += 'XC'
            elif num >= 50:
                num -= 50
                res += 'L'
            elif num >= 40:
                num -= 40
                res += 'XL'
            elif num >= 10:
                num -= 10
                res += 'X'
            elif num >= 9:
                num -= 9
                res += 'IX'
            elif num >= 5:
                num -= 5
                res += 'V'
            else:
                num -= 1
                res += 'I'
        return res

import nose

match = {1 : 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',  500: 'D', 1000: 'M'}

def test_int_to_roman():
    sol = Solution()
    assert sol.intToRoman(9) == 'IX', sol.intToRoman(9)
    assert sol.intToRoman(1954) == 'MCMLIV', sol.intToRoman(1954)
    assert sol.intToRoman(1990) == 'MCMXC', sol.intToRoman(1990)
    assert sol.intToRoman(2014) == 'MMXIV', sol.intToRoman(2014)

if __name__ == '__main__':
    nose.runmodule()
