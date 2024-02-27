# https://leetcode.com/problems/multiply-strings/
# Time: 1 hour 8 min 32 sec
# 287/311 testcases passed, time limit exceeded
# Time complexity O(n^2)
class Solution(object):
    def times_table(self, num1, num2):
        return str(int(num1) * int(num2))

    def add(self, num1, num2):
        # Add leading 0s to make string lengths match
        # and add an additional leading zero
        maxlen = max(len(num1),len(num2))
        num1 = "0" * (maxlen - len(num1) + 1) + num1
        num2 = "0" * (maxlen - len(num2) + 1) + num2
        summ = ["0" for _ in range(maxlen + 1)]
        for i in range(len(num1)-1, -1, -1):
            j = i
            while True:
                sumpart = int(num1[j]) + int(num2[j])
                sumpart += int(summ[j])
                summ[j] = str(sumpart)
                if sumpart >= 10:
                    summ[j] = str(int(summ[j]) - 10)
                    j = j - 1
                    summ[j] = str(int(summ[j]) + 1)
                    if int(summ[j]) <= 9:
                        break
                else:
                    break
        output = ''.join(summ)
        output = str(int(output)) # Remove leading 0s
        return output

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = ""
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                zeros = (len(num1) - i - 1) + (len(num2) - j - 1)
                product = self.times_table(num1[i],num2[j])
                product += "0" * zeros
                sum = self.add(product,sum)
        return sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply("81","81"))