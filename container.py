class Solution(object):
    def area(self, h1, h2, x1, x2):
        return min(h1, h2) * abs(x1 - x2)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        for i in range(len(height)):
            for j in range(len(height)):
                a = self.area(height[i], height[j], i, j)
                if a > m:
                    m = a
        return m

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,1]))