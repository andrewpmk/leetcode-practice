# https://leetcode.com/problems/zigzag-conversion/
# 14 min 56 sec
# Time complexity O(n)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s = s.replace(" ","")
        direction = 1  # 1 means going down, -1 means going up on diagonal
        row = 0
        array = [[] for _ in range(numRows)]
        for i in range(len(s)):
            array[row].append(s[i])
            if numRows > 1:
                row += direction
                if row == numRows - 1 or row == 0:
                    direction *= -1  # Reverse
        rows = []
        for i in range(len(array)):
            rows.append(''.join(array[i]))
        return ''.join(rows)

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("AB",1))