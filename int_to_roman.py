# https://leetcode.com/problems/integer-to-roman/
# Time elapsed: 59 min 19 sec

class Solution(object):
    numerals = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    magnitudes = (1, 10, 100, 1000)
    lookup = sorted(numerals.keys())

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        magnitude = 0
        # Break out smaller digits
        for i in self.magnitudes:
            if num >= i:
                magnitude = i
        multiply = num // magnitude
        major = multiply * magnitude
        minor = num % major
        if magnitude == 1000:
            roman = self.numerals[magnitude] * multiply
        elif multiply == 9:
            roman = self.numerals[magnitude] + self.numerals[self.lookup[self.lookup.index(magnitude)+2]]
        elif 6 <= multiply <= 8:
            roman = self.numerals[self.lookup[self.lookup.index(magnitude) + 1]]
            roman += self.intToRoman(major - 5*magnitude)
        elif multiply == 5:
            roman = self.numerals[self.lookup[self.lookup.index(magnitude) + 1]]
        elif multiply == 4:
            roman = self.numerals[magnitude] + self.numerals[self.lookup[self.lookup.index(magnitude)+1]]
        else:
            roman = self.numerals[magnitude] * multiply
        subroman = ""
        if minor > 0:
            subroman = self.intToRoman(minor)
        return roman + subroman


if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1999))
