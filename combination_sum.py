# https://leetcode.com/problems/combination-sum/
# Inefficient O(n^3) algorithm
# Gave up after 10 min - provides incorrect answer.
# In leetcode example you are allowed duplicates

import itertools

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = set()
        for length in range(1,len(candidates)+1):
            combos = list(itertools.combinations(candidates, length))
            for i in combos:
                sum = 0
                combo = []
                for j in range(len(i)):
                    sum += i[j]
                    combo.append(i[j])
                    if sum == target:
                        combo = sorted(combo)
                        output.add(tuple(combo))
                        break
        ret = []
        for i in output:
            ret.append(list(i))
        return ret

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,6,7],7))

