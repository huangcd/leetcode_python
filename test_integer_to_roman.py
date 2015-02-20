'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        return ''.join(self.yield_roman(num))

    def yield_roman(self, num):
        while num:
            if num >= 1000:
                yield 'M' * (num / 1000)
                num = num % 1000
            elif num >= 900:
                num -= 900
                yield 'CM'
            elif num >= 500:
                num -= 500
                yield 'D'
            elif num >= 400:
                num -= 400
                yield 'CD'
            elif num >= 100:
                yield 'C' * (num / 100)
                num = num % 100
            elif num >= 90:
                num -= 90
                yield 'XC'
            elif num >= 50:
                num -= 50
                yield 'L'
            elif num >= 40:
                num -= 40
                yield 'XL'
            elif num >= 10:
                yield 'X' * (num / 10)
                num = num % 10
            elif num >= 9:
                num -= 9
                yield 'IX'
            elif num >= 5:
                num -= 5
                yield 'V'
            elif num >= 4:
                num -= 5
                yield 'IV'
            else:
                yield 'I' * num
                num = 0
        raise StopIteration()

import nose

match = {1 : 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',  500: 'D', 1000: 'M'}

def test_int_to_roman():
    sol = Solution()
    assert sol.intToRoman(9) == 'IX', sol.intToRoman(9)
    assert sol.intToRoman(1954) == 'MCMLIV', sol.intToRoman(1954)
    assert sol.intToRoman(1990) == 'MCMXC', sol.intToRoman(1990)
    assert sol.intToRoman(2014) == 'MMXIV', sol.intToRoman(2014)
    assert sol.intToRoman(100) == 'C', sol.intToRoman(100)

if __name__ == '__main__':
    nose.runmodule()
