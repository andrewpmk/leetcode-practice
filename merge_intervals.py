# https://leetcode.com/problems/merge-intervals/
# Inefficient solution 30 min 29 sec

class Solution(object):
    def doesOverlap(self, interval1, interval2):
        if interval1[0] > interval2[0] and interval1[1] > interval2[1]:
            temp = interval1
            interval1 = interval2
            interval2 = temp
        if interval1[1] >= interval2[0]:
            return True
        return False

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Convert to set of tuples

        overlaps = -1
        while overlaps != 0:
            next = False
            overlaps = 0
            for i in range(len(intervals)):
                if next:
                    break
                for j in range(len(intervals)):
                    if i == j or i > j:
                        continue
                    if self.doesOverlap(intervals[i], intervals[j]):
                        overlaps += 1
                        new_intervals = []
                        minimum = min(intervals[i][0],intervals[j][0])
                        maximum = max(intervals[i][1],intervals[j][1])
                        new_intervals.append([minimum,maximum])
                        for k in range(len(intervals)):
                            if i != k and j != k:
                                new_intervals.append(intervals[k])
                        intervals = new_intervals
                        next = True
                        break
        return intervals

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1,4],[4,5]]))
    print(solution.doesOverlap([1,4],[0,4]))
