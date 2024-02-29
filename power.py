# https://leetcode.com/problems/powx-n/
# Inefficient solution by multiplying in 3 min 37 sec O(n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.myPow(x, -n)
        output = 1
        for i in range(n):
            output *= x
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2.1,3))
