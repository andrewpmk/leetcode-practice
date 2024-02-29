# https://leetcode.com/problems/pascals-triangle/
# Time 4 min 41 sec

class Solution(object):
    def generate_from_previous_row(self, previous_row):
        output = []
        for i in range(len(previous_row) + 1):
            if i == 0 or i == len(previous_row):
                output.append(1)
            else:
                output.append(previous_row[i-1] + previous_row[i])
        return output

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            if i == 0:
                output.append([1])
            else:
                output.append(self.generate_from_previous_row(output[-1]))
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))
