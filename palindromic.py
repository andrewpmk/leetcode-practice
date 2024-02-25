# https://leetcode.com/problems/longest-palindromic-substring/
# Time to create inefficient O(n^2) algorithm 3 min 53 sec

class Solution(object):
    def is_palindrome(self, s):
        return s[::-1] == s

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        output = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if j < i:
                    continue
                substring = s[i:j]
                if len(substring) > longest and self.is_palindrome(substring):
                    output = substring
                    longest = len(substring)
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("cbbd"))
