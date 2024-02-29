# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def hasNoRepeatingCharacters(self, s):
        l = list(s)
        return len(l) == len(set(l))

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        for left in range(len(s)):
            for right in range(len(s)-1,left-1,-1):
                if right-left+1 < maxlength:
                    break
                substr = s[left:right+1]
                if self.hasNoRepeatingCharacters(substr):
                    maxlength = right-left+1
                    break
        return maxlength


if __name__ == "__main__":
    solution = Solution()
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))
