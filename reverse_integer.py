# https://leetcode.com/problems/reverse-integer/
# Time to solve: 6 min 30 sec

class Solution(object):
    def reverse_string(self, s: str) -> str:
        output = ""
        for i in range(len(s) - 1, -1, -1):
            output += s[i]
        return output

    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        negative: bool = x < 0
        if negative:
            x = -x
        reversed = self.reverse_string(str(x))
        output = int(reversed)
        if negative:
            cutoff = 2**31
        else:
            cutoff = 2**31-1
        if output>cutoff:
            return 0
        if negative:
            return -output
        else:
            return output


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
