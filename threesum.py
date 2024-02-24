# https://leetcode.com/problems/3sum/
# 19 min 24 sec to get inefficient O(n^3) solution

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        # Here's the inefficient O(n^3) solution
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and i != j and i != k and j != k:
                        s.add(tuple(sorted([a, b, c])))
        output = []
        for i in s:
            output.append(list(i))
        return output


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))
